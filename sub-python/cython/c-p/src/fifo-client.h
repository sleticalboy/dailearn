//
// Created by binlee on 24-3-15.
//

#ifndef C_P_FIFO_CLIENT_H
#define C_P_FIFO_CLIENT_H

#include <string>
#include <fcntl.h>

class FifoClient {
private:
  int req_fd_;
  int resp_fd_;
public:
  FifoClient(const std::string &req_file, const std::string &resp_file) {
    this->req_fd_ = open(req_file.c_str(), O_WRONLY);
    this->resp_fd_ = open(resp_file.c_str(), O_RDONLY);
  }

  int send_req(const std::string& req_buf) const;

  std::string recv_resp() const;

  void close() {
    ::close(this->req_fd_);
    ::close(this->resp_fd_);
  }
};

#endif //C_P_FIFO_CLIENT_H
