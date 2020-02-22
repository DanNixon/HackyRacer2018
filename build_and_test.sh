#!/bin/bash

set -x

pushd './cad/'
pytest --verbose
./build_all.sh
popd

pushd './accessory_control_firmware/'
pio run
popd
