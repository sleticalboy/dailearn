package com.sleticalboy.myapplication;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.text.Html;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import com.google.gson.Gson;

import java.io.IOException;

import butterknife.ButterKnife;
import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.Response;
import okhttp3.ResponseBody;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ButterKnife.bind(this);
        setContentView(R.layout.activity_main);

        // 设置 stock View
        String url = "https://gupiao.baidu.com/api/rails/stockbasicbatch?format=json&stock_code=hk02799";
        HttpUtils.request(url, new Callback() {
            @Override
            public void onFailure(Call call, IOException e) {
                Toast.makeText(MainActivity.this, "网络异常", Toast.LENGTH_SHORT).show();
                e.printStackTrace();
            }

            @Override
            public void onResponse(Call call, Response response) throws IOException {
                ResponseBody vBody = response.body();
                if (vBody == null) {
                    return;
                }
                String vJson = vBody.string();
                if (vJson == null) {
                    return;
                }
                final Stock vStock = new Gson().fromJson(vJson, Stock.class);
                if (vStock.data != null && vStock.data.size() > 0) {
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            setStockView(vStock.data.get(0));
                        }
                    });
                }
            }
        });
    }

    private void setStockView(Stock.DataEntity stock) {
        TextView stockName = (TextView) findViewById(R.id.tv_stock_name);
        stockName.setText(stock.stockName);

        TextView stockCode = (TextView) findViewById(R.id.tv_stock_code);
        stockCode.setText(stock.stockCode);

        TextView stockNetchange = (TextView) findViewById(R.id.tv_stock_netchange);
        stockNetchange.setText(String.format("%s↑", stock.netChange));

        TextView stockNetchangeRatio = (TextView) findViewById(R.id.tv_stock_netchange_ratio);
        stockNetchangeRatio.setText(String.format("+%s%%", stock.netChangeRatio));

        TextView stockPreclose = (TextView) findViewById(R.id.tv_stock_preclose);
        CharSequence preClose = getText(R.string.yesterday_income);
        stockPreclose.setText(String.format(preClose.toString(), stock.preClose));

        TextView stockOpen = (TextView) findViewById(R.id.tv_stock_open);
        CharSequence open = getText(R.string.today_open_quotation);
        stockOpen.setText(Html.fromHtml(String.format(open.toString(), stock.open)));

        TextView stockHigh = (TextView) findViewById(R.id.tv_stock_high);
        CharSequence high = getText(R.string.highest_rise);
        stockHigh.setText(Html.fromHtml(String.format(high.toString(), stock.high)));

        TextView stockLow = (TextView) findViewById(R.id.tv_stock_low);
        CharSequence low = getText(R.string.lowest_rise);
        stockLow.setText(Html.fromHtml(String.format(low.toString(), stock.low)));
    }
}
