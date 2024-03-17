#include <cstdlib>
#include <csignal>
#include <cstdio>
#include <cerrno>
#include <string>
#include <sstream>
#include <unistd.h>
#include "lib_main.h"
#include "fifo-client.h"
#include "httplib.h"

extern "C" {
int main() {
  // return run_main_test();
  int pid = fork();
  if (pid < 0) { // err
    std::printf("%s() err: %d, %d\n", __func__, pid, errno);
    return errno;
  }
  if (pid == 0) { // child side
    auto cwd = getcwd(nullptr, 0);
    std::printf("%s() child pid: %d\n", __func__, pid);
    std::string cmd("python");
    cmd = cmd + " " + cwd + "/scripts/socket-server.py";
    std::printf("%s() start cmd: '%s'\n", __func__, cmd.c_str());
    auto res = std::system(cmd.c_str());
    std::printf("%s() cmd res: %d\n", __func__, res);
  } else { // parent side
    // 等待子进程启动
    sleep(1);
    std::printf("%s() parent pid: %d\n", __func__, pid);
    // // 启动 client
    // std::string REQ_NAME = "/home/binlee/code/Dailearn/sub-python/cython/c-p/testdata/request.txt";
    // std::string RESP_NAME = "/home/binlee/code/Dailearn/sub-python/cython/c-p/testdata/response.txt";
    // auto client = FifoClient(REQ_NAME, RESP_NAME);
    // int counter = 100;
    // while (counter) {
    //   std::stringstream ss;
    //   ss << "hello server " << (counter * 9569);
    //   auto size = client.send_req(ss.str());
    //   std::printf("send req buf: %d\n", size);
    //   auto resp_buf = client.recv_resp();
    //   std::printf("recv resp buf: %s\n", resp_buf.c_str());
    //   counter--;
    //   sleep(1);
    // }
    // client.close();
    httplib::Client cli("127.0.0.1", 50000);
    std::string body(R"({"key": "hello world"})");
    httplib::Headers headers{
        {"User-Agent",      "algo-client/1.0.00"},
        {"Connection",      "keep-alive"},
        {"Accept",          "*/*"},
        {"Accept-Encoding", "gzip, deflate"},
        {"Content-Type",    "application/json"},
        {"Content-Length",  std::to_string(body.size())},
    };
    int counter = 10;
    while (counter) {
      if (auto r = cli.Post("/predict", headers, body, "application/json")) {
        std::cout << r->status << ", " << r->reason << ", " << std::endl;
        for (const auto &h: r->headers) {
          std::cout << h.first << ": " << h.second << std::endl;
        }
        std::cout << r->body << std::endl;
        sleep(2);
        counter--;
      }
    }
  }
  return 0;
}
}
