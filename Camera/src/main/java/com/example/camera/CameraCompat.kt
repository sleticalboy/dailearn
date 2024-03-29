package com.example.camera

import android.content.Context
import android.util.Log
import android.view.SurfaceHolder
import com.example.camera.compat.CameraV1
import com.example.camera.compat.CameraV2
import com.example.camera.compat.ICamera

/**
 * Created by renlei
 * DATE: 15-11-5
 * Time: 下午4:57
 * Email: lei.ren@renren-inc.com
 */
class CameraCompat private constructor() {

    private var camera: ICamera
    private var mUseCamera1 = true

    init {
        camera = if (mUseCamera1) CameraV1() else CameraV2()
        Log.d(TAG, "init() called $camera")
    }

    fun setUseCameraV1(useCamera1: Boolean) {
        Log.d(TAG, "setUseCameraV1() called with: useCamera1 = $useCamera1")
        mUseCamera1 = useCamera1
    }

    fun init(context: Context) {
        Log.d(TAG, "init() called with: context = $context")
        camera.init(context)
    }

    fun open() {
        open(camera.getId())
    }

    /**
     * 打开相机
     *
     * @param id
     */
    fun open(id: Int) {
        Log.d(TAG, "open camera with id: $id")
        camera.open(id)
    }

    /**
     * 开启预览
     */
    fun startPreview(obj: Any?) {
        Log.d(TAG, "startPreview() called with: obj = $obj")
        if (obj == null) return
        camera.startPreview(obj)
    }

    /**
     * 结束预览
     */
    fun stopPreview() {
        Log.d(TAG, "stopPreview() called")
        camera.stopPreview()
    }

    /**
     * 拍照
     */
    fun doTakePic(callback: ICamera.TakePhotoCallback) {
        Log.d(TAG, "doTakePic() called with: callback = $callback")
        camera.takePhoto(callback)
    }

    /**
     * 点击聚焦
     */
    fun autoFocus(callback: ICamera.AutoFocusCallback?): Boolean {
        Log.d(TAG, "autoFocus() called with: callback = $callback")
        return camera.autoFocus(callback)
    }

    /**
     * 设置聚焦的区域
     */
    fun setFocusArea(rawX: Float, rawY: Float) {
        Log.d(TAG, "setFocusArea() called with: rawX = $rawX, rawY = $rawY")
        camera.setFocusArea(rawX, rawY)
    }

    /**
     * 设置闪光灯的模式
     */
    fun setFlashMode(chooser: ICamera.FlashModeChooser) {
        Log.d(TAG, "setFlashMode() called with: chooser = $chooser")
        camera.setFlashMode(chooser)
    }

    fun getId(): Int = camera.getId()

    companion object {
        private val sCamera = CameraCompat()
        private const val TAG = "CameraCompat"

        fun get(): CameraCompat {
            return sCamera
        }
    }
}