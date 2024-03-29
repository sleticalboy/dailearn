package com.sleticalboy.dailywork

import android.app.ListActivity
import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.ArrayAdapter
import android.widget.ListView
import android.widget.TextView
import com.sleticalboy.dailywork.anims.TransitionUI
import com.sleticalboy.dailywork.bt.BluetoothUI
import com.sleticalboy.dailywork.camera.LiveCameraActivity
import com.sleticalboy.dailywork.components.ServicePractise
import com.sleticalboy.dailywork.csv.AlphaActivity
import com.sleticalboy.dailywork.csv.AutoSwitchUI
import com.sleticalboy.dailywork.csv.CustomViewActivity
import com.sleticalboy.dailywork.csv.HeaderActivity
import com.sleticalboy.dailywork.debug.DebugUI
import com.sleticalboy.dailywork.devices.DeviceAdminUI
import com.sleticalboy.dailywork.others.AlarmActivity
import com.sleticalboy.dailywork.others.ImageConvertUI
import com.sleticalboy.dailywork.rv.ClassifyActivity
import com.sleticalboy.dailywork.rv.DecorationActivity
import com.sleticalboy.dailywork.rv.PagerActivity
import com.sleticalboy.dailywork.rv.WheelRVActivity

/**
 * Created on 18-1-29.
 *
 * @author leebin
 * @version 1.0
 * @description 启动界面
 */
class StartActivity : ListActivity() {

    private val dataList = arrayOf(
            // debug tools
            ItemHolder(DebugUI::class.java, "调试工具"),
            // bluetooth
            ItemHolder(BluetoothUI::class.java, "蓝牙模块"),
            // device admin
            ItemHolder(DeviceAdminUI::class.java, "设备管理"),
            // components
            ItemHolder(ServicePractise::class.java, "Service"),
            // animations
            ItemHolder(TransitionUI::class.java, "转场动画"),
            // custom View & // special effects of View
            ItemHolder(AutoSwitchUI::class.java, "自动切换View使用"),
            ItemHolder(GreenDaoActivity::class.java, "GreenDao 数据库框架使用"),
            ItemHolder(CustomViewActivity::class.java, "自定义 View"),
            ItemHolder(HeaderActivity::class.java, "头部悬停效果"),
            ItemHolder(AlphaActivity::class.java, "控件透明度"),
            // camera
            ItemHolder(LiveCameraActivity::class.java, "TextureView 实现实时预览"),
            // Bitmap
            ItemHolder(ImageConvertUI::class.java, "图片和字符串相互转换"),
            // Tasks
            ItemHolder(AlarmActivity::class.java, "定时任务"),
            // RecyclerView
            ItemHolder(ClassifyActivity::class.java, "RecyclerView 分类别显示"),
            ItemHolder(PagerActivity::class.java, "RecyclerView 分页"),
            ItemHolder(DecorationActivity::class.java, "RecyclerView 添加 item 分割线 / 拖拽排序"),
            ItemHolder(WheelRVActivity::class.java, "RecyclerView 轮播"),
            ItemHolder(PullRefreshActivity::class.java, "下拉刷新库测试"),
            ItemHolder(RefreshActivity::class.java, "下拉刷新 View"),
            ItemHolder(PullRefreshActivity::class.java, "下拉刷新库测试")
            ItemHolder(WheelRVActivity::class.java, "RecyclerView 轮播")
    )

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val listAdapter = ArrayAdapter(this,
                android.R.layout.simple_list_item_1, dataList)
        setListAdapter(listAdapter)
    }

    override fun onListItemClick(l: ListView, v: View, position: Int, id: Long) {
        val holder = dataList[position]
        (v as TextView).text = holder.mName
        startActivity(Intent(this, holder.mClass))
    }

    class ItemHolder(internal var mClass: Class<*>, internal var mName: String) {

        override fun toString(): String {
            return mName
        }
    }
}
