cmake_minimum_required(VERSION 3.5)
project(c-p)

# 指定 C 编译器
#set(CMAKE_C_COMPILER clang)
# 指定 C++ 编译器
#set(CMAKE_CXX_COMPILER clang++)

include_directories(
        /usr/include/python3.8
        /usr/include/google/protobuf
        /src/cc
)

link_directories(
        /usr/lib/x86_64-linux-gnu/
        /usr/lib/
)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})

# 编译二进制程序
add_executable(sample
        src/main.cc
        src/lib_main.cc
        src/cc/algo.pb.cc
        src/cc/algox.pb.cc
        src/cc/py_algo.pb.cc
        src/cc/audio_whisper.pb.cc
        src/fifo-client.cpp src/fifo-client.h
        )
target_link_libraries(sample python3.8 protobuf)

add_executable(socket-client src/socket-client.cpp)
