#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <cstring>
#include <csignal>
#include <cstdio>
#include <cerrno>
#include <string>
#include <unistd.h>

#include "httplib.h"

int socket_client() {
  // 1、创建客户端
  int fd = socket(AF_INET, SOCK_STREAM, 0);
  sockaddr_in server_addr;
  memset(&server_addr, 0, sizeof(server_addr));
  server_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
  server_addr.sin_family = AF_INET;
  server_addr.sin_port = htons(50000);
  // 2、连接服务端
  int res = connect(fd, (sockaddr *) &server_addr, sizeof(server_addr));
  if (res != 0) {
    std::printf("connect failed, res: %d, err: %d\n", res, errno);
    return res;
  }
  while (true) {
    // status line
    std::string req_buf = "POST /predict HTTP/1.1\r\n";
    // headers
    req_buf += "User-Agent: algo-client/1.0.00\r\n";
    req_buf += "Connection: keep-alive\r\n";
    req_buf += "Accept: */*\r\n";
    req_buf += "Accept-Encoding: gzip, deflate\r\n";
    req_buf += "Content-Type: application/json\r\n";
    req_buf += "Content-Length: 22\r\n";
    req_buf += "\r\n";
    // body
    req_buf += R"({"key": "hello world"})";
    req_buf += "\r\n\r\n";
    // end
    size_t size = send(fd, req_buf.c_str(), req_buf.size(), 0);
    std::printf("send: %zu, %s\n", size, req_buf.c_str());

    std::string resp_buf;
    char buf[4096];
    while (true) {
      memset(buf, 0, sizeof(buf));
      if (recv(fd, buf, sizeof(buf) - 1, 0) <= 0) {
        break;
      }
      resp_buf.append(buf);
    }
    std::printf("recv >>>: %zu, %s\n", resp_buf.size(), resp_buf.c_str());
    sleep(10);
  }
  close(fd);
  std::printf("close fd: %d\n", fd);
  return 0;
}


int main() {
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
  while (true) {
    if (auto r = cli.Post("/predict", headers, body, "application/json")) {
      std::cout << r->status << ", " << r->reason << ", " << std::endl;
      for (const auto &h: r->headers) {
        std::cout << h.first << ": " << h.second << std::endl;
      }
      std::cout << r->body << std::endl;
      sleep(20);
    }
  }
  return 0;
}