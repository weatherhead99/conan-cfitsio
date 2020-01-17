project(test_cfitsio)
cmake_minimum_required(VERSION 3.6)

include("${CMAKE_BINARY_DIR}/conanbuildinfo.cmake")
conan_basic_setup(TARGETS)

message(STATUS "testing find cfitsio manually in cmake")
find_library(cmake_cfitsio cfitsio)
message(STATUS "location of found library: ${cmake_cfitsio}")

if(NOT cmake_cfitsio)
  message(FATAL_ERROR "couldn't find cfitsio at all!")
endif()

get_filename_component(cfitsio_path ${cmake_cfitsio} DIRECTORY)

if(NOT ${cfitsio_path} STREQUAL ${CONAN_LIB_DIRS_CFITSIO})
  message(FATAL_ERROR "found cfitsio but it isn't the one from conan!")
endif()

message(STATUS "testing linking test program via conan mechanism")
add_executable(test_cfitsio main.cpp)
target_link_libraries(test_cfitsio CONAN_PKG::cfitsio)
