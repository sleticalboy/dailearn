import logging
import os
import socket
import time


def run_server():
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


if __name__ == '__main__':
    run_server()
