package com.sleticalboy.myapplication;

import java.io.Serializable;
import java.util.List;

/**
 * Created by AS on 18-1-29.
 *
 * @author sleticalboy
 * @version 1.0
 * @description 股票实体类
 */
public class Stock implements Serializable {

    public int errorNo;
    public String errorMsg;
    public List<DataEntity> data;

    public static class DataEntity {
        public String stockCode;
        public String stockName;
        public String exchange;
        public int asset;
        public String stockStatus;
        public double close;
        public double high;
        public double low;
        public long capitalization;
        public int netChange;
        public int netChangeRatio;
        public int volume;
        public double amplitudeRatio;
        public double turnoverRatio;
        public double preClose;
        public double open;
        public int followNum;
    }
}
