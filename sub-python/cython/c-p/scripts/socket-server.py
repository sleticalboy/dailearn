import json
import logging
import os
import sys
import time

from http.server import (HTTPServer, BaseHTTPRequestHandler)


def run_server():
    import socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 50000))
    server.listen(5)
    conn, addr = server.accept()
    logging.warning(f'conn: {conn}, addr: {addr}')
    while 1:
        req_buf = conn.recv(1024)
        if req_buf:
            # 模拟耗时操作
            time.sleep(1.5)
            req_buf = req_buf[:-1].decode()
            logging.warning(f'<<<: {req_buf}')
            resp_buf = f'{req_buf}, pid: {os.getpid()}\x00'.encode()
            size = conn.send(resp_buf)
            logging.warning(f'send {size}, buf: {resp_buf}')
        pass
    server.close()
    pass


def _ansi_style(value: str, *styles: str) -> str:
    codes = {
        "bold": 1,
        "red": 31,
        "green": 32,
        "yellow": 33,
        "magenta": 35,
        "cyan": 36,
    }

    for style in styles:
        value = f"\x1b[{codes[style]}m{value}"

    return f"{value}\x1b[0m"


class RequestHandler(BaseHTTPRequestHandler):

    server = HTTPServer
    #  url 处理器
    _handlers = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __getattr__(self, name: str):
        # 拦截所有 http 请求，自行处理
        if name.startswith('do_'):
            logging.warning(f"{self.__class__.__name__}#__getattr__('{name}')")
            return self._process_request
        return getattr(super(), name)

    def _process_request(self):
        logging.warning(f'{self.command} {self.path}, {self.headers}, {self._handlers}')
        handler = self._handlers.get(self.command, {}).get(self.path)
        if handler:
            return handler(self)
        raise Exception(f"Unknown '{self.command}' '{self.path}'")

    @classmethod
    def register(cls, method, rule, h):
        cls._handlers.setdefault(method, {}).setdefault(rule, h)


def healthy(r):
    logging.warning(f'{r.command} {r.path}, {r.headers}')

    resp_buf = json.dumps({'code': 0, 'msg': 'OK'})
    # 1、response line
    r.send_response(200, 'OK')
    # 2、response headers
    r.send_header('Content-Type', 'application/json')
    r.send_header('Content-Length', str(len(resp_buf)))
    r.send_header('Connection', 'keep-alive')
    r.end_headers()
    # 3、response body
    r.wfile.write(resp_buf.encode('UTF-8', 'replace'))
    pass


def predict(r):
    logging.warning(f'{r.command} {r.path}, {r.headers}')

    size = int(r.headers.get('Content-Length'))
    buf = r.rfile.read(size)
    logging.warning(f'req buf: {buf}')

    resp_buf = None
    try:
        from google.protobuf import __version__
        logging.warning(f'proto version: {__version__}')
        import algox_pb2, algo_pb2, audio_whisper_pb2
        from py_algo_pb2 import PyAlgoRequest, PyAlgoResponse
        from audio_whisper_pb2 import AudioWhisperRequest, AudioWhisperResponse
        py_req = PyAlgoRequest()
        py_req.ParseFromString(buf)

        logging.error(f'py req buf: {py_req.request_buf}')

        whisper_req = AudioWhisperRequest()
        whisper_req.ParseFromString(py_req.request_buf)

        logging.error(f'urls: {py_req.download_urls}, whisper req: {whisper_req}')

        py_resp = PyAlgoResponse()
        whisper_resp = AudioWhisperResponse()
        whisper_resp.op_type = whisper_req.op_type
        whisper_resp.language = whisper_req.language
        whisper_resp.full_text = 'hello world'
        whisper_resp.text_start_ts = 20
        whisper_resp.text_end_ts = 30000
        whisper_resp.out_json_url = 'hello'
        py_resp.upload_urls.kvs.get_or_create("hello").url = "world"
        py_resp.response_buf = whisper_resp.SerializeToString()
        resp_buf = py_resp.SerializeToString()
    except BaseException as e:
        logging.exception(e)
    finally:
        pass

    # resp_buf = json.dumps({'code': 0, 'msg': 'OK'})
    r.send_response(200, 'OK')

    r.send_header('Content-Type', 'application/protobuf')
    r.send_header('Content-Length', str(len(resp_buf)))
    r.send_header('Connection', 'keep-alive')
    r.end_headers()
    # r.wfile.write(resp_buf.encode('UTF-8', 'replace'))
    r.wfile.write(resp_buf)
    pass


if __name__ == '__main__':
    RequestHandler.register('GET', '/healthz', healthy)
    RequestHandler.register('POST', '/predict', predict)
    server = HTTPServer(('127.0.0.1', 50000), RequestHandlerClass=RequestHandler)
    server.serve_forever()
    pass
