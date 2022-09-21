package com.example.plugin;

import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class PluginActivity extends AppCompatActivity {

  private static final String TAG = "PluginActivity";

  @Override public void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    // TODO: 2022/9/21 这里实际显示的是 alarm_activity，资源冲突了，要解决
    // int layout activity_main 0x7f0b001c
    // int layout activity_alarm 0x7f0b001c
    setContentView(R.layout.activity_main);
    Log.d(TAG, "onCreate() " + getApplication() + ", res: " + getApplication().getResources());
    new Handler().postDelayed(() -> {
      Toast.makeText(this, "Hello Plugin", Toast.LENGTH_SHORT).show();
    }, 500L);
  }

  @Override
  protected void onStart() {
    super.onStart();
    Log.d(TAG, "onStart() called");
  }

  @Override
  protected void onResume() {
    super.onResume();
    Log.d(TAG, "onResume() called");
  }

  @Override
  protected void onPause() {
    super.onPause();
    Log.d(TAG, "onPause() called");
  }

  @Override
  protected void onStop() {
    super.onStop();
    Log.d(TAG, "onStop() called");
  }

  @Override
  protected void onDestroy() {
    super.onDestroy();
    Log.d(TAG, "onDestroy() called");
  }
}