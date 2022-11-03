package com.example.dyvd.engine;

import android.util.Log;
import com.example.dyvd.DyUtil;
import com.example.dyvd.VideoItem;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import org.json.JSONException;
import org.json.JSONObject;

/**
 * Created on 2022/11/3
 *
 * @author binlee
 */
public final class DyEngine extends Engine {

  public static final String DOMAIN = "v.douyin.com";
  public static final String TOOL_URL = "https://www.ilovetools.cn/douyin/search-video-info";

  public DyEngine(String text) {
    super(text);
  }

  // 1.20 VLj:/ “别让这个城市留下了你的青春，却留不下你”# 离开 # 城市 # 回乡 # 逃离北上广 # 服务员 # 生活 https://v.douyin.com/MxFGWAS/ 复制此链接，打开Dou音搜索，直接观看视频！
  // 2.56 usR:/ 北漂13年，失败告终，带着一身疲惫光荣返乡！踏踏实实做个农民吧！老房改造第一季~# 旧房改造 # 老房改造# 农村生活# 返乡创业青年 https://v.douyin.com/MxFHfSB/ 复制此链接，打开Dou音搜索，直接观看视频！
  // 2.58 lcn:/ 复制打开抖音，看看【返乡军哥的作品】北漂13年，失败告终，带着一身疲惫光荣返乡！踏踏实... https://v.douyin.com/M9VCxkn/
  // title: 北漂13年，失败告终，带着一身疲惫光荣返乡！踏踏实...
  // author: 返乡军哥的作品
  // url: https://v.douyin.com/M9VCxkn/
  @Override protected String parseShareUrl(String text) {
    // 校验域名
    if (text == null || !text.contains(DOMAIN)) return null;

    // 解析 url
    int start = text.indexOf("http");
    if (start < 0) return null;
    final int end = text.lastIndexOf('/');
    return end < 0 ? text.substring(start) : text.substring(start, end + 1);
  }

  @Override protected String getVideoInfo() throws IOException, JSONException {
    final HttpURLConnection connection = (HttpURLConnection) new URL(TOOL_URL).openConnection();
    connection.setRequestMethod("POST");
    connection.addRequestProperty("Accept", "*/*");
    connection.addRequestProperty("Host", "www.ilovetools.cn");
    connection.addRequestProperty("Origin", "https://www.ilovetools.cn");
    connection.addRequestProperty("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8");
    connection.addRequestProperty("User-Agent", USER_AGENT);
    connection.setDoOutput(true);
    connection.getOutputStream().write(("shareUrl=" + shareUrl).getBytes());
    final int code = connection.getResponseCode();
    Log.d(TAG, "getVideoInfo() http code: " + code + ", msg: [" + connection.getResponseMessage()
      + "], mime: " + connection.getContentType());
    // stream to string
    String result;
    if (code >= 200 && code < 400) {
      result = DyUtil.streamAsString(connection.getInputStream());
    } else {
      result = DyUtil.streamAsString(connection.getErrorStream());
    }
    return new JSONObject(result).getString("data");
  }

  @Override protected VideoItem fromJson(String shareUrl, String text) {
    try {
      final JSONObject json = new JSONObject(text);
      // desc: 不怕反派坏，就怕反派帅#萌宠 #赵文卓 #画画 #变装
      // title: 不怕反派坏，就怕反派帅
      // tags: #萌宠 #赵文卓 #画画 #变装
      final VideoItem item = new VideoItem();
      item.shareUrl = shareUrl;
      final String desc = json.getString("desc");
      int index;
      if ((index = desc.indexOf('#')) >= 0) {
        item.title = desc.substring(0, index);
        item.tags = desc.substring(index);
      } else {
        item.title = desc;
      }
      item.coverUrl = json.getString("imgUrl");
      item.url = json.getString("videoUrl");
      item.bgmUrl = json.getString("musicUrl");
      return item;
    } catch (JSONException e) {
      Log.w(TAG, "fromJson() invalid json: " + text);
      return null;
    }
  }
}
