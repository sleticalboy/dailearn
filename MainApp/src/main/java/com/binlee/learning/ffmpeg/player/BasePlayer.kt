package com.binlee.learning.ffmpeg.player

import android.media.AudioFormat
import android.media.AudioManager
import android.media.AudioTrack
import android.os.Handler
import android.os.Looper
import android.os.SystemClock
import android.util.Log
import com.binlee.learning.ffmpeg.AVFormat
import com.binlee.learning.ffmpeg.AVFormat.A_PCM
import com.binlee.learning.ffmpeg.IPlayer
import com.binlee.learning.ffmpeg.IPlayer.Callback
import com.binlee.learning.ffmpeg.IPlayer.State
import com.binlee.learning.ffmpeg.IPlayer.State.PAUSED
import com.binlee.learning.ffmpeg.IPlayer.State.PLAYING
import com.binlee.learning.ffmpeg.IPlayer.State.STOPPED
import com.binlee.learning.ffmpeg.Packet
import java.io.RandomAccessFile
import java.util.LinkedList
import kotlin.concurrent.thread

/**
 * Created on 2023/3/20
 *
 * @author binlee
 */
open class BasePlayer(protected val format: AVFormat = A_PCM): IPlayer {

  protected val TAG = javaClass.simpleName
  private lateinit var path: String
  private var track: AudioTrack? = null
  private val queueLock = Object()
  private val queue = LinkedList<Packet>()
  private val innerCallback = object: Callback {
    private val handler = Handler(Looper.getMainLooper())
    override fun onState(state: State) {
      handler.post { userCallback?.onState(state) }
    }
  }
  private var userCallback: Callback? = null

  override fun setInputFile(path: String) {
    this.path = path
  }

  override fun start(callback: Callback) {
    if (track != null) return

    userCallback = callback

    val size = AudioTrack.getMinBufferSize(44100, AudioFormat.CHANNEL_OUT_MONO, AudioFormat.ENCODING_PCM_16BIT) * 2

    // mTrack = AudioTrack(
    //   AudioAttributes.Builder()
    //     .setLegacyStreamType(AudioManager.STREAM_MUSIC)
    //     .build(),
    //   AudioFormat.Builder()
    //     .setChannelMask(AudioFormat.CHANNEL_OUT_MONO)
    //     .setSampleRate(44100)
    //     .setEncoding(AudioFormat.ENCODING_PCM_16BIT)
    //     .build(),
    //   size, AudioTrack.MODE_STREAM, AudioManager.AUDIO_SESSION_ID_GENERATE
    // )
    track = AudioTrack(
      AudioManager.STREAM_MUSIC,
      44100,
      AudioFormat.CHANNEL_OUT_MONO,
      AudioFormat.ENCODING_PCM_16BIT,
      size,
      AudioTrack.MODE_STREAM
    )
    track!!.play()
    innerCallback.onState(PLAYING)

    // player thread
    thread(start = true, name = "$TAG-thread") {
      Log.e(TAG, "player thread enter!")
      while (true) {
        if (!isPlaying()) {
          SystemClock.sleep(250L)
          continue
        }

        val packet = dequeuePacket()

        if (packet == null || packet.size < 0) {
          Log.e(TAG, "player thread: EOF!")
          break
        }
        // Log.i(TAG, "player thread: write pcm size: ${packet.size}")
        val written = track!!.write(packet.buffer, 0, packet.size)
        if (written < 0) {
          Log.e(TAG, "player thread: write audio data failed: $written")
          break
        }
      }
      Log.e(TAG, "player thread exit!")
      track!!.release()
      track = null
      innerCallback.onState(STOPPED)
    }

    val input = RandomAccessFile(path, "r")

    // reader(encoder) thread
    thread(start = true, name = "Reader-thread") {
      Log.e(TAG, "reader thread enter!")
      onReaderStarted(input)

      val buffer = ByteArray(1024)
      while (true) {
        if (readFile(input, buffer)/*eof*/) break
      }
      input.close()

      Log.e(TAG, "reader thread exit!")
      onReaderStopped()
    }
  }

  override fun pause() {
    // pause -> play(resume)
    if (isPlaying()) {
      // 不会立即暂停，会在写入数据全部播放完成之后暂停
      // mTrack!!.stop()

      // 立即暂停，不会丢弃已写入数据，下次继续播放
      track!!.pause()
      // 丢弃已写入但未播放的数据
      // mTrack!!.flush()
      innerCallback.onState(PAUSED)
      return
    }
  }

  override fun resume() {
    if (isPaused()) {
      track!!.play()
      innerCallback.onState(PLAYING)
      return
    }
  }

  override fun isPlaying(): Boolean {
    return track?.playState == AudioTrack.PLAYSTATE_PLAYING
  }

  override fun isPaused(): Boolean {
    return track?.playState == AudioTrack.PLAYSTATE_PAUSED
  }

  protected open fun onReaderStarted(input: RandomAccessFile) {
  }

  protected open fun onReaderStopped() {
  }

  protected open fun readFile(input: RandomAccessFile, buffer: ByteArray): Boolean/*eof*/ {
    val readBytes = input.read(buffer)
    enqueuePacket(Packet(buffer, readBytes))
    return readBytes < 0
  }

  protected fun enqueuePacket(packet: Packet) {
    synchronized(queueLock) {
      var timer = 0
      while (queue.size >= 4) {
        queueLock.wait()
        timer++
      }
      Log.e(TAG, "enqueuePacket() wait queue $timer times")
      queue.addFirst(packet)
      queueLock.notifyAll()
    }
  }

  private fun dequeuePacket(): Packet? {
    synchronized(queueLock) {
      var timer = 0
      while (queue.size == 0) {
        queueLock.wait(250L)
        timer++
      }
      Log.e(TAG, "dequeuePacket() wait queue $timer times")
      val packet = queue.removeLast()
      queueLock.notifyAll()
      return packet
    }
  }
}