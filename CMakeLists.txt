cmake_minimum_required(VERSION 3.0)

project(tracy)

set(CMAKE_CXX_STANDARD 11)

option(TRACY_ENABLE "Profiling is enabled" ON)

add_library(tracy_client TracyClient.cpp)
add_library(tracy_client_dll TracyClientDLL.cpp)

if(TRACY_ENABLE)
    target_compile_definitions(tracy_client PUBLIC TRACY_ENABLE)
    target_compile_definitions(tracy_client_dll PUBLIC TRACY_ENABLE)
endif()

target_include_directories(tracy_client     PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}")
target_include_directories(tracy_client_dll PUBLIC "${CMAKE_CURRENT_SOURCE_DIR}")
