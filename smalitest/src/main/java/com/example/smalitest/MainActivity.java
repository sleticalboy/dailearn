package com.example.smalitest;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;

import androidx.annotation.Nullable;

import java.security.SecureRandom;

public class MainActivity extends Activity {

  private static final String TAG = "MainActivity";

  @Override
  protected void onCreate(@Nullable Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    String androidId = Long.toHexString(new SecureRandom().nextLong());
    Log.d(TAG, new StringBuilder("onCreate() android id: ").append(androidId).toString());
    Log.d(TAG, new StringBuilder("onCreate() id: ").append(zzbx.zza(this)).toString());
  }
}
