//
// Created by binlee on 3/15/24.
//
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

#include <cstring>
#include <sstream>

#define REQ_NAME "/home/binlee/code/Dailearn/sub-python/cython/c-p/testdata/request.txt"
#define RESP_NAME "/home/binlee/code/Dailearn/sub-python/cython/c-p/testdata/response.txt"

// client
int main() {
  int req_fd = open(REQ_NAME, O_WRONLY | O_NONBLOCK);
  int resp_fd = open(RESP_NAME, O_RDONLY | O_NONBLOCK);

  int seq = 0;
  char buffer[1024]; // 定义接受的文件大小，可以设大点，1024*1024*n
  while (true) {
    size_t n;
    // 发送请求
    std::stringstream ss;
    ss << "Hello, fifo server! " << seq++;
    int retries = 10;
    while (retries > 0) {
      n = write(req_fd, ss.str().c_str(), ss.str().length() + 1);
      if (n > 0) {
        std::printf("send req buf len: %zu -> %s\n", n, ss.str().c_str());
        break;
      }
      retries--;
      usleep(15000);
    }
    if (retries <= 0) break;

    // 接收响应
    while (true) {
      memset(buffer, 0, sizeof(buffer));
      n = read(resp_fd, buffer, sizeof(buffer));
      if (n > 0) {
        printf("recv resp buf: %s, len: %zu\n", buffer, n);
        break;
      }
      usleep(5000);
    }
  }
  close(req_fd);
  close(resp_fd);
  return 0;
}
