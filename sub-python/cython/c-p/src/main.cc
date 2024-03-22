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
#include "cc/py_algo.pb.h"
#include "cc/audio_whisper.pb.h"
#include "cc/algo.pb.h"

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
    const char *new_argv[4];
    new_argv[0] = "sh";
    new_argv[1] = "-c";
    new_argv[2] = cmd.c_str();
    new_argv[3] = nullptr;
    int res = execv("/usr/bin/sh", (char *const *) new_argv);
    std::printf("%s() cmd res: %d\n", __func__, res);
    return 0;
  } else { // parent side
    // 等待子进程启动
    sleep(1);
    std::printf("%s() parent pid: %d\n", __func__, pid);
    httplib::Client cli("127.0.0.1", 50000);

    py_algopb::PyAlgoRequest py_req{};
    py_req.set_algo_name("prj-parse");
    py_req.set_proto_version("3.20.3");
    audio_whisperpb::AudioWhisperRequest whisper_req{};
    whisper_req.set_language("en");
    whisper_req.set_op_type(audio_whisperpb::Whisper);
    whisper_req.set_audio_url("https://www.example.com/demo.wav");
    whisper_req.set_model_size("medium");
    py_req.set_request_buf(whisper_req.SerializeAsString());

    algopb::AlgoDownloadUrlMap urls{};
    urls.mutable_kvs()->insert({"https://www.example.com/a.index", {}});
    urls.mutable_kvs()->insert({"https://www.example.com/b.index", {}});
    urls.mutable_kvs()->insert({"https://www.example.com/c.index", {}});
    py_req.mutable_download_urls()->Swap(&urls);

    std::string req_buf;
    py_req.SerializeToString(&req_buf);

    httplib::Headers headers{
        {"User-Agent",      "algo-client/1.0.00"},
        {"Connection",      "closer"},
        {"Accept",          "*/*"},
        {"Accept-Encoding", "gzip, deflate"},
        {"Content-Length",  std::to_string(req_buf.size())},
    };
    int counter = 3;
    std::printf("0....\n");
    while (counter) {
      if (auto r = cli.Post("/predict", headers, req_buf, "application/protobuf")) {
        std::printf("1.... %s, len: %zu\n", r->version.c_str(), r->content_length_);
        std::cout << r->status << ", " << r->reason << ", " << std::endl;
        for (const auto &h: r->headers) {
          std::cout << h.first << ": " << h.second << std::endl;
        }
        // std::cout << r->body << std::endl;

        py_algopb::PyAlgoResponse py_resp{};
        py_resp.ParseFromString(r->body);
        std::cout << "py resp: " << py_resp.ShortDebugString() << std::endl;
        audio_whisperpb::AudioWhisperResponse whisper_resp{};
        whisper_resp.ParseFromString(py_resp.response_buf());
        std::cout << "whisper resp: " << whisper_resp.ShortDebugString() << std::endl;
        std::printf("2....\n");
        usleep(0.5 * 1e6);
        std::printf("3....\n");
        counter--;
        std::printf("4....\n");
      }
    }
    std::printf("5....\n");
  }
  std::printf("exit....\n");
  return 0;
}
}
