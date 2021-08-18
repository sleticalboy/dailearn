package com.sleticalboy.learning

import android.content.Intent
import android.graphics.Color
import android.util.Log
import android.view.Gravity
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.sleticalboy.bean.Apis
import com.sleticalboy.http.IDemo
import com.sleticalboy.http.RetrofitClient
import com.sleticalboy.learning.base.BaseActivity
import com.sleticalboy.learning.bean.ModuleItem
import com.sleticalboy.learning.data.DataEngine
import com.sleticalboy.learning.data.Result
import com.sleticalboy.learning.databinding.ActivityIndexBinding
import io.reactivex.schedulers.Schedulers
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import kotlin.concurrent.thread

class IndexActivity : BaseActivity() {

    private val dataSet = arrayListOf<ModuleItem>()
    private var mBind: ActivityIndexBinding? = null

    override fun layout(): View {
        // R.layout.activity_index
        mBind = ActivityIndexBinding.inflate(layoutInflater)
        return mBind!!.root
    }

    override fun initView() {
        mBind!!.recyclerView.adapter = DataAdapter(dataSet)
        val start = System.currentTimeMillis()
        DataEngine.get().indexModel().getModuleSource().observe(this, {
            when (it) {
                is Result.Loading -> {
                    Log.d(logTag(), "initView() loading data: $it")
                }
                is Result.Error -> {
                    Log.d(logTag(), "initView() load data error: $it")
                }
                else -> {
                    Log.d(logTag(), "initView() load data success: $it")
                    dataSet.clear()
                    dataSet.addAll((it as Result.Success).getData())
                    mBind!!.recyclerView.adapter?.notifyItemRangeChanged(0, dataSet.size - 1)
                    Log.d(logTag(), "show UI cost: ${System.currentTimeMillis() - start} ms")
                }
            }
        })
    }

    override fun initData() {
        // baidu()
        github()
    }

    private fun github() {
        thread {
            val service = RetrofitClient.get().create(IDemo::class.java)
            service.listApis().enqueue(object : Callback<Apis> {
                override fun onResponse(call: Call<Apis>, response: Response<Apis>) {
                    Log.v(logTag(), "response: ${response.body()}")
                }

                override fun onFailure(call: Call<Apis>, t: Throwable) {
                    Log.e(logTag(), "error: $t")
                }
            })
        }
    }

    private fun baidu() {
        thread {
            val demo = RetrofitClient.get().create(IDemo::class.java)
            val result = demo.visit("text/html").execute().body()
            Log.v(logTag(), "retrofit result: $result")

            demo.visit().subscribeOn(Schedulers.io())
                .observeOn(Schedulers.io())
                .subscribe {
                    Log.v(logTag(), "rxjava result: $it")
                }

            Log.v(logTag(), "list result: " + demo.list())
            val array = demo.byteArray()
            Log.v(logTag(), "byte array result: " + array.size + " " + String(array))

            val webPage = demo.webPage()
            Log.v(logTag(), "web page result: $webPage")
        }

    }

    override fun logTag(): String = "IndexActivity"

    override fun onDestroy() {
        super.onDestroy()
        mBind = null
    }

    class DataAdapter(private val dataSet: ArrayList<ModuleItem>) :
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
                Log.d(TAG, "item click with: ${item.clazz}")
                holder.itemView.context.startActivity(Intent(holder.itemView.context, item.clazz))
            }
        }
    }

    class ItemHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {

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
        private const val TAG = "IndexActivity"
    }
}