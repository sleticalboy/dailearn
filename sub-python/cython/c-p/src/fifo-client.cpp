//
// Created by binlee on 3/15/24.
//
#include <cstring>
#include <unistd.h>

#include "fifo-client.h"

int FifoClient::send_req(const std::string& req_buf) const {
  return (int) write(this->req_fd_, req_buf.c_str(), req_buf.size() + 1);
}

std::string FifoClient::recv_resp() const {
  char buffer[1024]; // 定义接受的文件大小，可以设大点，1024*1024*n
  while (true) {
    memset(buffer, 0, sizeof(buffer));
    if (read(this->resp_fd_, buffer, sizeof(buffer)) > 0) {
      break;
    }
    usleep(5000);
  }
  return {buffer};
}
