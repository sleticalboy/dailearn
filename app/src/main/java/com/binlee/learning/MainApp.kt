package com.binlee.learning

import android.app.Application
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.os.Build
import android.util.Log
import com.binlee.dl.DlManager
import com.binlee.learning.components.receiver.GlobalReceiver
import com.binlee.learning.util.NotificationHelper

/**
 * Created on 18-3-5.
 *
 * @author leebin
 * @version 1.0
 */
class MainApp : Application() {

  override fun onCreate() {
    super.onCreate()
    // DlManager.get().init(this)
    mApp = this
    adaptAndroidO()
  }

<<<<<<< HEAD:MainApp/src/main/java/com/sleticalboy/learning/MainApp.kt
<<<<<<< HEAD:MainApp/src/main/java/com/sleticalboy/learning/MainApp.kt
  private fun adaptAndroidO() {
=======
  override fun getResources(): Resources {
    return DlManager.resources()
  }

  override fun getAssets(): AssetManager {
    return DlManager.resources().assets
  }

=======
>>>>>>> 90f26f9c (reat: virtual runtime via didi's VirtualApk):MainApp/src/main/java/com/binlee/learning/MainApp.kt
  private fun registerNotificationChannels() {
>>>>>>> 661d1ff1 (feat: hook ActivityThread#mInstrumentation to start a plugin activity):MainApp/src/main/java/com/binlee/learning/MainApp.kt
    if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) return
    Log.d("MainApp", "adapt android O")
    registerReceivers()
    NotificationHelper.createAllChannels(this)
  }

  private fun registerReceivers() {
    val intentFilter = IntentFilter()
    intentFilter.addAction(Intent.ACTION_SCREEN_ON)
    intentFilter.addAction(Intent.ACTION_USER_PRESENT)
    registerReceiver(GlobalReceiver(), intentFilter)
  }

  companion object {

    private const val TAG = "MainApp"

    private var mApp: Application? = null

    val app: Context? get() = mApp
  }
}
