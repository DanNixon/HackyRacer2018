#!/bin/sh

mkdir -p build && cd build
conan install -s compiler.libcxx=libstdc++11 ..
cmake ..
make -j4
