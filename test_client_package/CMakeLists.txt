cmake_minimum_required(VERSION 3.0)

project(test_tracy_client_package)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_BINARY_DIR}")

find_package(tracy_client REQUIRED)

add_executable(example example.cpp)
target_link_libraries(example PRIVATE tracy_client::tracy_client)
