#!/bin/bash

set -x

pushd 'cad/'
pytest --verbose
./build_all.sh
popd

pushd 'firmware/accessory_control/'
pio run
popd
