cmake_minimum_required(VERSION 3.10)

project(dashboard_lib_tests)

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")
include(GoogleTest)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

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
    GTest::Main
  )
endfunction()

add_unit_test(numeric_value_test)
add_unit_test(value_test)
