package com.binlee.learning

import android.app.Application
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.content.res.AssetManager
import android.content.res.Resources
import android.os.Build
import android.util.Log
import android.view.View
import android.view.ViewGroup
import com.binlee.learning.components.receiver.GlobalReceiver
import com.binlee.learning.util.NotificationHelper
import java.security.SecureRandom


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
    registerNotificationChannels()

    // Curtains.onRootViewsChangedListeners += OnRootViewsChangedListener { view, added ->
    //   Log.d(TAG, "root $view ${if (added) "added" else "removed"}")
    //   if (added) dumpChildren(view)
    // }

    val androidId = java.lang.Long.toHexString(SecureRandom().nextLong())
    Log.d(TAG, "onCreate() android id: $androidId")
  }

  private fun dumpChildren(root: View) {
    Log.d(TAG, "dumpChildren() $root")
    if (root is ViewGroup) {
      for (i in 0 until root.childCount) {
        dumpChildren(root.getChildAt(i))
      }
    }
  }

  private fun adaptAndroidO() {}

  override fun getResources(): Resources {
    // return DlManager.get().resources
    return super.getResources()
  }

  override fun getAssets(): AssetManager {
    // return DlManager.resources().assets
    return super.getAssets()
  }

  private fun registerNotificationChannels() {
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
