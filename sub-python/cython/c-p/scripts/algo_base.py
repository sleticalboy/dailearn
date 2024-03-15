import sys
from abc import abstractmethod


class CHelper:
    pass


class AlgoProcBase(object):
    """
    1、在 proto 中定义算法通用入参和结果并分别编译生成 python 和 c 源文件；
    2、c 将入参序列化为 proto 字节数组并送入 python 接口处理；
    3、python 将处理结果序列化为 proto 字节数组返回给 c；
    4、c 解析处理结果并转成结构体返回给 go；
    """

    # 回调函数
    callback = None

    def __init__(self):
        self.name = self.__class__.__name__
        self.callback = None

        from google.protobuf import __version__
        print(f'proto version: {__version__}')

        from py_algo_pb2 import PyAlgoRequest, PyAlgoResponse
        self.py_req = PyAlgoRequest()
        self.py_res = PyAlgoResponse()
        from algo_pb2 import AlgoDownloadUrlMap, AlgoUploadUrlMap
        self.download_urls = AlgoDownloadUrlMap()
        self.upload_urls = AlgoUploadUrlMap()
        print(f'[{self.name}]#__init__(), sys.path: {sys.path}')
        self.req_buf = b''
        self.resp_buf = b''
        pass

    def init(self, req_buf):
        self.py_req.ParseFromString(req_buf)
        self.download_urls.ParseFromString(self.py_req.download_urls_buf)
        self.name = self.py_req.algo_name
        self.req_buf = self.py_req.request_buf
        print(f"[{self.name}]#init(), type: {type(req_buf)}, buf: {req_buf}")

    @classmethod
    def set_callback(cls, callback):
        """
        给算法设置回调函数
        :param callback: 回调函数
        """
        cls.callback = callback
        print(f'{cls.__name__}#set_callback({callback})')

    def on_progress(self, progress):
        """
        回调算法进度，如果有的话
        :param progress: 进度
        """
        if self.callback and hasattr(self.callback, 'on_progress'):
            self.callback.on_progress(progress)

    def generate_path(self, suffix: str = None, additional: str = None) -> str:
        """
        生成文件路径
        :param suffix: 文件后缀，为空时会生成一个目录，否则生成一个文件路径
        :param additional: 额外的信息，会附带在路径中
        :return: 文件路径
        """
        if self.callback and hasattr(self.callback, 'gen_path'):
            return self.callback.gen_path(additional=additional, suffix=suffix)
        raise Exception("callback is not set, could not generate path")

    def process(self):
        """
        算法处理
        :return: 处理结果
        """
        print(f'{self.name}#process()')
        self.process_impl()
        self.py_res.upload_urls_buf = self.upload_urls.SerializeToString()
        self.py_res.response_buf = self.resp_buf
        return self.py_res.SerializeToString(), 'proto'

    def process_impl(self):
        pass

    @abstractmethod
    def release(self):
        """
        释放算法资源
        """
        print(f'{self.name}#process()')
