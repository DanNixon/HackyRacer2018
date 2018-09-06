cmake_minimum_required(VERSION 3.5)

project(dashboard_lib_tests)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(NO_OUTPUT_DIRS)

enable_testing()

function(UnitTest TEST_NAME)
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
    ${CONAN_LIBS_GTEST}
  )
endfunction()

UnitTest(numeric_value_test)
UnitTest(value_test)
