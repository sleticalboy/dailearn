#include <arpa/inet.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <cstring>
#include <csignal>
#include <cstdio>
#include <cerrno>
#include <string>

int main() {
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
    std::string req_buf = "POST /predict HTTP/1.0\r\n";
    req_buf += "\r\n";
    // headers
    req_buf += "Connection: keep-alive\r\n";
    req_buf += "Accept: application/json\r\n";
    req_buf += "\r\n";
    // body
    req_buf += "hello world\r\n";
    req_buf += "\r\n";
    // end
    size_t size = send(fd, req_buf.c_str(), req_buf.size() + 1, 0);
    std::printf("send: %s, %zu\n", req_buf.c_str(), size);
    char buf[1024];
    size = recv(fd, buf, sizeof(buf), 0);
    std::printf("recv >>>: %s, %zu\n", buf, size);
    sleep(1);
  }
  close(fd);
  std::printf("close fd: %d\n", fd);
  return 0;
}