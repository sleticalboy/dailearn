import os
import time

TEST_ROOT = os.path.dirname(os.path.dirname(__file__))
TEST_ROOT = os.path.join(TEST_ROOT, 'testdata')


# server

def recv_req(req_fd):
    while 1:
        buf = os.read(req_fd, 1024)[:-1].decode()
        if buf:
            break
        time.sleep(0.5)
    print(f"{__name__}#recv_req(): {buf}")
    return buf


def handle_req(req_buf):
    return f'echo: {req_buf}'


def send_resp(resp_fd, resp_buf):
    try:
        os.write(resp_fd, str.encode(resp_buf))
        print(f"send resp: {resp_buf}")
    except:
        print("client closed, exit!")
        return False
    return True


def TestIFIO():
    req_file = os.path.join(TEST_ROOT, "request.txt")
    resp_file = os.path.join(TEST_ROOT, "response.txt")
    os.system(f'rm {req_file} {resp_file};touch {req_file}; touch {resp_file}')

    # 1.create fifo
    if not os.path.exists(req_file):
        os.mkfifo(req_file, 0o666)
    if not os.path.exists(resp_file):
        os.mkfifo(resp_file, 0o666)

    # 2.open pipe 不加 os.O_NONBLOCK 会一直阻塞
    print('init write pipe: ' + resp_file)
    resp_fd = os.open(resp_file, os.O_WRONLY | os.O_NONBLOCK)
    print('init read pipe:  ' + req_file)
    req_fd = os.open(req_file, os.O_RDONLY | os.O_NONBLOCK)

    # 3.write and read data
    while 1:
        # 接收请求
        req_buf = recv_req(req_fd)
        # 处理请求
        resp_buf = handle_req(req_buf)
        # 发送响应
        if not send_resp(resp_fd, resp_buf):
            break
        time.sleep(1.5)

    os.close(req_fd)
    os.close(resp_fd)


if __name__ == '__main__':
    TestIFIO()
