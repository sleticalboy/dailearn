package com.sleticalboy.http;

import androidx.annotation.NonNull;
import androidx.annotation.WorkerThread;
<<<<<<< HEAD:Http/src/main/java/com/sleticalboy/http/OkDownloader.java

import com.sleticalboy.http.builder.GetBuilder;
import com.sleticalboy.http.builder.RequestBuilder;
import com.sleticalboy.http.callback.DownloadCallback;
import com.sleticalboy.http.callback.ProgressCallback;
import com.sleticalboy.http.interceptor.ProgressInterceptor;

=======
import com.binlee.http.builder.GetBuilder;
import com.binlee.http.builder.RequestBuilder;
import com.binlee.http.callback.DownloadCallback;
import com.binlee.http.callback.ProgressCallback;
import com.binlee.http.interceptor.ProgressInterceptor;
>>>>>>> d3b061e1 (style: improve code style):Http/src/main/java/com/binlee/http/OkDownloader.java
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.RandomAccessFile;

import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.Response;
import okhttp3.ResponseBody;

/**
 * Created on 18-9-19.
 *
 * @author leebin
 */
public final class OkDownloader {
    
    private static final int STATE_RESUME = 0x100;
    private static final int STATE_PAUSE = 0x101;
    private static final int STATE_CANCEL = 0x102;
    
    private final String mUrl;
    private final File mSaveFile;
    private DownloadCallback mCallback;
    private boolean mIsPause = false;
    private boolean mIsCancel = false;
    private boolean mIsDownloading = false;
    /*** 断点的位置 ***/
    private long breakPoint = 0L;
    
    public OkDownloader(String downloadUrl, String savePath) {
        this(downloadUrl, new File(savePath), false);
    }
    
    public OkDownloader(String downloadUrl, File saveFile, boolean isNeedProgress) {
        mUrl = downloadUrl;
        mSaveFile = saveFile;
        if (isNeedProgress) {
            HttpClient.get().addInterceptor(ProgressInterceptor.newInstance());
            ProgressInterceptor.addCallback(mUrl, new ProgressCallback.SimpleCallback() {
                
                @Override
                public void onPreExecute(long total) {
                    if (mCallback != null) {
                        // 断点续传时此处为剩余文件的长度
                        // total + breakPoint 是文件的总长度
                        HttpClient.get().getMainHandler().post(() -> mCallback.onStart(total));
                    }
                }
                
                @Override
                public void onProgress(float progress, long bytesTotalRead) {
                    if (mCallback != null) {
                        HttpClient.get().getMainHandler().post(() -> mCallback.onProgress(progress));
                    }
                }
            });
        }
    }
    mIsCancel = false;
    mIsPause = false;
    download(0L);
  }

  /**
   * 开始下载
   *
   * @param startPoint 位置
   */
  private void download(final long startPoint) {
    RequestBuilder getBuilder = new GetBuilder()
      .url(mUrl)
      .breakPoint(startPoint, null);
    HttpClient.get().getOkHttpClient().newCall(getBuilder.build()).enqueue(new Callback() {
      @Override
      public void onFailure(@NonNull final Call call, @NonNull final IOException e) {
        if (mCallback != null) {
            if (state == STATE_CANCEL) {
                HttpClient.get().getMainHandler().post(() -> mCallback.onCancel());
            } else if (state == STATE_PAUSE) {
                HttpClient.get().getMainHandler().post(() -> mCallback.onPause());
            } else if (state == STATE_RESUME) {
                HttpClient.get().getMainHandler().post(() -> mCallback.onResume());
            }
        }
      }

      @Override
      public void onResponse(@NonNull final Call call, @NonNull final Response response) {
        final ResponseBody responseBody = response.body();
        if (response.isSuccessful() && responseBody != null) {
          saveFile(responseBody, startPoint);
        }
        mIsPause = true;
        mIsCancel = false;
        mIsDownloading = false;
    }
    
    /**
     * 恢复下载
     */
    public void resume() {
        if (mIsDownloading) {
            return;
        }
        mIsDownloading = true;
        mIsPause = false;
        mIsCancel = false;
        notifyStateChange(STATE_RESUME);
        download(breakPoint);
    }
    
    /**
     * 设置回调, before {@link OkDownloader#start()}
     *
     * @param callback {@link DownloadCallback}
     */
    public void setDownloadCallback(DownloadCallback callback) {
        mCallback = callback;
    }
    
    /**
     * 取消下载
     */
    public void cancel() {
        if (mIsCancel) {
            return;
        }
      }
      if (mCallback != null) {
        ProgressInterceptor.removeCallback(mUrl);
        resetDownloader();
        HttpClient.get().getMainHandler().post(() -> mCallback.onComplete(mSaveFile));
      }
    } catch (IOException e) {
      if (mCallback != null) {
        HttpClient.get().getMainHandler().post(() -> mCallback.onError(e));
      }
    } finally {
      OkUtils.closeSilently(inputStream);
      OkUtils.closeSilently(randomAccessFile);
    }
}
