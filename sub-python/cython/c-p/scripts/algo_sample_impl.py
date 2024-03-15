import logging
import os

from algo_base import AlgoProcBase


class GoLib:

    def __init__(self):
        lib_path = '/home/binlee/code/Golearn/go-so/libfib.so'
        import ctypes
        self.lib = ctypes.cdll.LoadLibrary(lib_path)

    def say_hello(self, msg):
        self.lib.HelloGo(bytes(msg))


def err_4():
    raise Exception('sample exception')


def err_3():
    err_4()


def err_2():
    err_3()


def err_1():
    err_2()


class AlgoProcImpl(AlgoProcBase):
    """
    1、在 proto 中定义算法通用入参和结果并分别编译生成 python 和 c 源文件；
    2、c 将入参序列化为 proto 字节数组并送入 python 接口处理；
    3、python 将处理结果序列化为 proto 字节数组返回给 c；
    4、c 解析处理结果并转成结构体返回给 go；
    """

    def __init__(self):
        super().__init__()

    def process_impl(self):
        super().process_impl()
        from audio_whisper_pb2 import AudioWhisperRequest, AudioWhisperResponse
        req = AudioWhisperRequest()
        req.ParseFromString(self.req_buf)
        logging.warning(f'request is: {req}')

        resp = AudioWhisperResponse()
        resp.language = req.language
        resp.audio_duration = 3000
        resp.out_json_url = req.audio_url[0:req.audio_url.rfind('.')] + '.json'
        resp.op_type = resp.op_type
        logging.warning(f'response is: {resp}')
        self.upload_urls.kvs.setdefault(resp.out_json_url)
        self.resp_buf = resp.SerializeToString()

    def release(self):
        print(f"[{self.name}]#release()")


if __name__ == '__main__':
    test_data = os.path.abspath(os.getcwd() + "/../testdata")
    from py_algo_pb2 import PyAlgoRequest, PyAlgoResponse
    from algo_pb2 import AlgoDownloadUrlMap

    _proc = AlgoProcImpl()
    _req = PyAlgoRequest()
    _req.algo_name = 'prj-export'
    from audio_whisper_pb2 import AudioWhisperRequest

    awr = AudioWhisperRequest()
    awr.op_type = 0
    awr.audio_url = 'http://example.com/a.wav'
    awr.model_size = 'medium'
    _req.request_buf = awr.SerializeToString()
    urls = AlgoDownloadUrlMap()
    urls.kvs.setdefault(awr.audio_url)
    _req.download_urls_buf = urls.SerializeToString()
    _proc.init(_req.SerializeToString())
    _rep_buf, _fmt = _proc.process()
    _proc.release()
    _rep = PyAlgoResponse()
    _rep.ParseFromString(_rep_buf)
    print(f'output {type(_rep)} -> {_rep.__str__()}')
