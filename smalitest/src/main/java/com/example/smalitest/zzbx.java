package com.example.smalitest;

import android.content.ContentResolver;
import android.content.Context;
import android.os.Build;
import android.provider.Settings;

import androidx.core.os.EnvironmentCompat;

import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;

/* compiled from: com.google.android.ump:user-messaging-platform@@2.0.0 */
/* loaded from: classes.dex */
public final class zzbx {
  private static String zza;

  public static synchronized String zza(Context context) {
    String str;
    synchronized (zzbx.class) {
      if (zza == null) {
        ContentResolver contentResolver = context.getContentResolver();
        String tmp = contentResolver == null ? null : Settings.Secure.getString(contentResolver, "android_id");
        if (tmp == null || zzb()) {
          tmp = Long.toHexString(new SecureRandom().nextLong());
        }
        zza = zzc(tmp);
      }
      str = zza;
    }
    return str;
  }

  public static boolean zzb() {
    if (Build.FINGERPRINT.startsWith("generic") || Build.FINGERPRINT.startsWith(EnvironmentCompat.MEDIA_UNKNOWN) || Build.MODEL.contains("google_sdk") || Build.MODEL.contains("Emulator") || Build.MODEL.contains("Android SDK built for x86") || Build.MANUFACTURER.contains("Genymotion")) {
      return false;
    }
    return ((!Build.BRAND.startsWith("generic") || !Build.DEVICE.startsWith("generic")) && "google_sdk".equals(Build.PRODUCT)) ? false : false;
  }

  private static String zzc(String str) {
    for (int i = 0; i < 3; i++) {
      try {
        MessageDigest instance = MessageDigest.getInstance("MD5");
        instance.update(str.getBytes());
        return String.format("%032X", new BigInteger(1, instance.digest()));
      } catch (ArithmeticException unused) {
        return "";
      } catch (NoSuchAlgorithmException unused2) {
      }
    }
    return "";
  }
}
