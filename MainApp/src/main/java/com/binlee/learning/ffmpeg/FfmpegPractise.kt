package com.binlee.learning.ffmpeg

import android.Manifest.permission
import android.content.Intent
import android.content.pm.PackageManager
import android.graphics.Color
import android.media.AudioFormat
import android.media.AudioRecord
import android.media.MediaRecorder.AudioSource
import android.os.Build.VERSION
import android.os.Build.VERSION_CODES
import android.provider.MediaStore.Video.Media
import android.util.Log
import android.view.Gravity
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import android.widget.Toast
import androidx.core.app.ActivityCompat
import androidx.recyclerview.widget.RecyclerView
import com.binlee.learning.R
import com.binlee.learning.base.BaseActivity
import com.binlee.learning.bean.ModuleItem
import com.binlee.learning.databinding.ActivityListItemBinding
import com.example.ffmpeg.FfmpegHelper
import java.io.File
import java.io.FileOutputStream
import java.io.OutputStream

/**
 * Created on 2022/8/3
 *
 * @author binlee
 */
class FfmpegPractise : BaseActivity() {

  // java 中的构造代码块
  init {
    //
  }

  private var mBind: ActivityListItemBinding? = null
  private val dataSet = arrayListOf(
    ModuleItem("打印媒体 meta 信息", "dump_meta"),
    ModuleItem("音频提取", "extract_audio"),
    ModuleItem("音频录制", "record_audio"),
  )

  private var flag: String? = null

  override fun layout(): View {
    mBind = ActivityListItemBinding.inflate(layoutInflater)
    return mBind!!.root
  }

  override fun initView() {
    mBind?.recyclerView?.adapter = DataAdapter(dataSet)
    Toast.makeText(this, ffmpegVersions, Toast.LENGTH_LONG).show()
  }

  private fun onClickItem(item: ModuleItem) {
    Log.d(TAG, "item click with: ${item.title}")
    if (item.cls == "record_audio") {
      startRecordAudio()
    } else {
      flag = item.cls
      // 打开相册选视频
      val intent = Intent(Intent.ACTION_PICK).setType("video/*")
      startActivityForResult(intent, PICK_VIDEO)
    }
  }

  private var mRecordThread: Thread? = null
  private var mRecordFile: OutputStream? = null

  private fun startRecordAudio() {
    Log.d(TAG, "startRecordAudio()")
    Toast.makeText(this, "\"startRecordAudio()\"", Toast.LENGTH_SHORT).show()
    if (ActivityCompat.checkSelfPermission(this, permission.RECORD_AUDIO) != PackageManager.PERMISSION_GRANTED) {
      ActivityCompat.requestPermissions(this, arrayOf(permission.RECORD_AUDIO), 0x44100)
      return
    }
    // 构造 AudioRecord
    val size = AudioRecord.getMinBufferSize(44100, AudioFormat.CHANNEL_IN_MONO, AudioFormat.ENCODING_PCM_8BIT)
    val record = AudioRecord(AudioSource.MIC, 44100, AudioFormat.CHANNEL_IN_MONO, AudioFormat.ENCODING_PCM_8BIT, size)
    // 开始录音
    record.startRecording()
    // 开启子线程从 audio buffer 中读取数据
    mRecordThread = Thread {
      val buffer = ByteArray(size)
      while (true) {
        val readBytes = record.read(buffer, 0, buffer.size)
        if (readBytes <= 0) {
          record.release()
          mRecordFile?.close()
          mRecordFile = null
          Log.d(TAG, "startRecordAudio() record over!")
          break
        }

        // 写入文件
        writeBuffer(buffer, readBytes)
      }
    }
    mRecordThread?.start()
    // 什么时候结束？暂时这样吧
    mBind?.root?.postDelayed({
      record.stop()
    }, 3_000L)
  }

  private fun writeBuffer(buffer: ByteArray, readBytes: Int) {
    if (mRecordFile == null) {
      // /storage/emulated/0/Android/data/com.binlee.learning/files/audio/
      val file = "${getExternalFilesDir("audio")}/${System.currentTimeMillis()}.pcm"
      mRecordFile = FileOutputStream(file)
      Log.d(TAG, "writeBuffer() create file: $file")
    }
    if (readBytes > 0) {
      mRecordFile?.write(buffer, 0, readBytes)
      mRecordFile?.flush()
      Log.d(TAG, "writeBuffer() size: $readBytes")
    }
  }

  override fun onRequestPermissionsResult(requestCode: Int, permissions: Array<out String>, grantResults: IntArray) {
    super.onRequestPermissionsResult(requestCode, permissions, grantResults)
    if (requestCode == 0x44100 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
      startRecordAudio()
    }
  }

  @Deprecated("Deprecated in Java")
  override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
    super.onActivityResult(requestCode, resultCode, data)
    if (requestCode == PICK_VIDEO && resultCode == RESULT_OK) {
      Log.d(TAG, "onActivityResult() video url: ${data?.data}")
      if (data?.data == null) return

      val columns = listOf(Media.DATA, Media.WIDTH, Media.HEIGHT)
      //从系统表中查询指定Uri对应的照片
      try {
        contentResolver.query(data.data!!, columns.toTypedArray(), null, null, null).use { cursor ->
          cursor!!.moveToFirst()
          // 获取媒体绝对路径
          val filepath = cursor.getString(0)
          Log.d(TAG, "onActivityResult() url: $data, path: $filepath")
          if ("dump_meta" == flag) {
            FfmpegHelper.dumpMetaInfo(filepath)
          } else if ("extract_audio" == flag) {
            // 输出文件路径
            val output = File(getExternalFilesDir(null), "${System.currentTimeMillis()}.aac")
            if (output.exists()) output.delete()
            output.createNewFile()

            val res = FfmpegHelper.extractAudio(filepath, output.absolutePath)
            // 提取音频数据之后，打印 meta 信息
            if (res == 0) FfmpegHelper.dumpMetaInfo(output.absolutePath)
            // output.delete()
          }
        }
      } catch (e: Throwable) {
        e.printStackTrace()
      }
    }
  }

  private inner class DataAdapter(private val dataSet: ArrayList<ModuleItem>) :
    RecyclerView.Adapter<ItemHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemHolder {
      val itemView = TextView(parent.context)
      itemView.setBackgroundResource(R.drawable.module_item_bg)
      return ItemHolder(itemView)
    }

    override fun getItemCount(): Int {
      return dataSet.size
    }

    override fun onBindViewHolder(holder: ItemHolder, position: Int) {
      val item = dataSet[position]
      holder.textView.text = item.title
      holder.textView.setOnClickListener {
        onClickItem(item)
      }
    }
  }

  private class ItemHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {

    val textView = itemView as TextView

    init {
      textView.gravity = Gravity.CENTER
      textView.layoutParams = ViewGroup.LayoutParams(
        ViewGroup.LayoutParams.MATCH_PARENT,
        ViewGroup.LayoutParams.WRAP_CONTENT
      )
      textView.setPadding(32, 16, 32, 16)
      textView.textSize = 24F
      textView.setTextColor(Color.BLUE)
    }
  }

  companion object {
    private const val TAG = "FfmpegPractise"
    private const val PICK_VIDEO = 0x1001

    private val ffmpegVersions: String = FfmpegHelper.getVersions()

  }
}