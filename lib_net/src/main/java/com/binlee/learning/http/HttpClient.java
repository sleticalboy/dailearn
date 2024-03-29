package com.binlee.learning.http;

import android.os.Handler;
import android.os.Looper;
import androidx.annotation.NonNull;
import com.alibaba.fastjson.JSON;
import com.binlee.learning.http.builder.DeleteBuilder;
import com.binlee.learning.http.builder.GetBuilder;
import com.binlee.learning.http.builder.PatchBuilder;
import com.binlee.learning.http.builder.PostBuilder;
import com.binlee.learning.http.builder.PutBuilder;
import com.binlee.learning.http.builder.RequestBuilder;
import com.binlee.learning.http.callback.HttpCallback;
import com.binlee.learning.http.cookie.CookieJarImpl;
import com.binlee.learning.http.interceptor.LoggerInterceptor;
import com.binlee.learning.http.ssl.Https;
import java.io.IOException;
import java.util.concurrent.TimeUnit;
import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.Interceptor;
import okhttp3.OkHttpClient;
import okhttp3.Response;
import okhttp3.ResponseBody;

/**
 * Created on 18-9-3.
 *
 * @author leebin
 */
public final class HttpClient {

  private static final boolean DBG = true;

  private static final HttpClient HTTP = new HttpClient();

  private final Handler mUi;
  private OkHttpClient mHttp;

  private HttpClient() {
    mUi = new Handler(Looper.getMainLooper());
    internalInit();
  }

  private void internalInit() {
    if (mHttp != null) {
      return;
    }
    final OkHttpClient.Builder builder = new OkHttpClient.Builder();
    builder.connectTimeout(30, TimeUnit.SECONDS);
    builder.readTimeout(30, TimeUnit.SECONDS);
    builder.writeTimeout(30, TimeUnit.SECONDS);
    builder.cookieJar(CookieJarImpl.ALL_COOKIE);
    builder.retryOnConnectionFailure(true);
    builder.eventListener(new DefaultEventListener());
    // builder.dispatcher(new Dispatcher());
    // builder.pingInterval(10000, TimeUnit.MILLISECONDS);
    // builder.connectionSpecs(Arrays.asList(ConnectionSpec.MODERN_TLS, ConnectionSpec.COMPATIBLE_TLS));
    // 还不支持某些网站的 https, 在查找原因
    // final Https.SSLParams sslParams = Https.getSSLParams(null, "ca");
    // builder.sslSocketFactory(sslParams.sslSocketFactory, sslParams.trustManager);
    // 不安全
    builder.hostnameVerifier(Https.trustAll());

    // 拦截器
    if (DBG) {
      final LoggerInterceptor loggerInterceptor = new LoggerInterceptor()
        .setLevel(LoggerInterceptor.Level.BODY);
      builder.addInterceptor(loggerInterceptor);
    }
    // builder.addInterceptor(ProgressInterceptor.newInstance()); // 下载的时候会用到
    // builder.addInterceptor(InjectHeaderInterceptor.newInstance()); // 用于 header 注入
    // builder.addInterceptor(GzipResponseInterceptor.newInstance()); // gzip 压缩解压缩

    // final boolean vpnEnable = Monitor.get().isVpnEnable(ContextProvider.getContext());
    // if (vpnEnable) {
    //     // 初始化时设置一次代理
    //     builder.proxy(OkUtils.createProxy(8011));
    //     Monitor.get().setProxyPortChangeCallback(new OnProxyPortChangeCallback.SimpleCallback() {
    //         @Override public void onProxyPortChange(int port) {
    //             // 当代理服务器端口发生变化时重置代理
    //             // mHttp = rebuildWithProxy(OkUtils.createProxy(port));
    //             mHttp = mHttp.newBuilder().proxy(OkUtils.createProxy(port)).build();
    //         }
    //     });
    // }
    mHttp = builder.build();
  }

  // private OkHttpClient rebuildWithProxy(Proxy proxy) {
  //     return mHttp.newBuilder().proxy(proxy).build();
  // }

  public static HttpClient get() {
    return HTTP;
  }

  public OkHttpClient getOkHttpClient() {
    checkInitialize();
    return mHttp.newBuilder().build();
  }

  private void checkInitialize() {
    if (mHttp == null) {
      internalInit();
    }
  }

  /**
   * 添加拦截器
   *
   * @param interceptor {@link Interceptor}
   * @return {@link HttpClient}
   */
  public HttpClient addInterceptor(Interceptor interceptor) {
    checkInitialize();
    mHttp.interceptors().add(interceptor);
    return this;
  }

  // public <T> void asyncExecute(retrofit2.Call<String> call, HttpCallback<T> callback) {
  //     call.enqueue(new retrofit2.Callback<String>() {
  //
  //         @SuppressWarnings("unchecked")
  //         @Override
  //         public void onResponse(final retrofit2.Call<String> call, final retrofit2.Response<String> response) {
  //             if (callback != null && response != null) {
  //                 final String result = response.body();
  //                 Object object;
  //                 if (callback.isStringType()) {
  //                     object = result;
  //                 } else {
  //                     object = JSON.parseObject(result, callback.getType());
  //                 }
  //                 mUi.post(() -> callback.onSuccess((T) object));
  //                 OkUtils.releaseCall(call);
  //             }
  //         }
  //
  //         @Override
  //         public void onFailure(final retrofit2.Call<String> call, final Throwable t) {
  //             if (callback != null) {
  //                 mUi.post(() -> callback.onFailure(t));
  //             }
  //             OkUtils.releaseCall(call);
  //         }
  //     });
  // }

  /**
   * 执行异步网络请求
   *
   * @param <T> 请求返回类型
   * @param builder {@link RequestBuilder} see also {@link GetBuilder}, {@link PostBuilder},
   * {@link PutBuilder}, {@link DeleteBuilder}, {@link PatchBuilder}
   * @param callback {@link HttpCallback} 网络请求回调[都已经回调到了主线程]
   */
  public <T> void request(@NonNull RequestBuilder builder, HttpCallback<T> callback) {
    checkInitialize();
    mHttp.newCall(builder.build()).enqueue(new Callback() {
      @Override
      public void onFailure(final Call call, final IOException e) {
        if (callback != null) {
          mUi.post(() -> callback.onFailure(e));
        }
        OkUtils.releaseCall(call);
      }

      @SuppressWarnings("unchecked")
      @Override
      public void onResponse(final Call call, final Response response) throws IOException {
        if (response.isSuccessful()) {
          final ResponseBody responseBody = response.body();
          if (callback != null && responseBody != null) {
            final String result = responseBody.string();
            final T object = callback.isStringType()
              ? (T) result
              : JSON.parseObject(result, callback.getType());
            mUi.post(() -> callback.onSuccess(object));
          }
        } else {
          final Exception error = new Exception(String.format("[code: %d, message: %s]%s",
            response.code(), response.message(), response.body().string()));
          if (callback != null) {
            mUi.post(() -> callback.onFailure(error));
          }
        }
        OkUtils.releaseCall(call);
      }
    });
  }

  public Handler getMainHandler() {
    checkInitialize();
    return mUi;
  }

  public void callbackError(com.binlee.learning.http.Callback callback, IOException e) {
    if (callback == null) return;
    mUi.post(() -> callback.onError(e));
  }
}
