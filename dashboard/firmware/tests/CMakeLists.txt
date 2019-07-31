cmake_minimum_required(VERSION 3.10)

project(dashboard_lib_tests)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
   message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
   file(DOWNLOAD "https://github.com/conan-io/cmake-conan/raw/v0.14/conan.cmake"
                 "${CMAKE_BINARY_DIR}/conan.cmake")
endif()
include(${CMAKE_BINARY_DIR}/conan.cmake)

conan_cmake_run(
  BASIC_SETUP
  CMAKE_TARGETS
  NO_OUTPUT_DIRS
  BUILD missing
  REQUIRES
    gtest/1.8.1@bincrafters/stable
)

enable_testing()

function(add_unit_test TEST_NAME)
  add_executable(
    ${TEST_NAME}
    tests/${TEST_NAME}.cpp
  )

  add_test(${TEST_NAME} ${TEST_NAME})

  target_include_directories(
    ${TEST_NAME}
    PRIVATE
    ${CMAKE_SOURCE_DIR}/../src
  )

  target_link_libraries(
    ${TEST_NAME}
    CONAN_PKG::gtest
  )
endfunction()

add_unit_test(numeric_value_test)
add_unit_test(value_test)
