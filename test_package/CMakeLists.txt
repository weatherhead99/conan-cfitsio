project(test_cfitsio)
cmake_minimum_required(VERSION 3.6)

include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
conan_basic_setup()


message(STATUS "testing find cfitsio via find_package")


add_executable(test_cfitsio main.cpp)
