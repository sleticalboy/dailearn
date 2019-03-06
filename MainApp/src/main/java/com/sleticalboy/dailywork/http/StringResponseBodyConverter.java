package com.sleticalboy.dailywork.http;

import java.io.IOException;

import okhttp3.ResponseBody;
import retrofit2.Converter;

/**
 * Created on 18-3-26.
 *
<<<<<<< HEAD
 * @author sleticalboy
 * @description
=======
 * @author leebin
>>>>>>> e43c101 (移除一些组件)
 */
public final class StringResponseBodyConverter<T> implements Converter<ResponseBody, T> {

    public StringResponseBodyConverter() {
    }

    @Override
    public T convert(ResponseBody value) throws IOException {
        return (T) value.string();
    }
}
