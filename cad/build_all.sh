#!/bin/bash

set -e

build_dir="$PWD/build"

function make_scad {
  module="$1"
  part="$2"

  out="$build_dir/$part"
  mkdir -p "$(dirname "$out")"

  scad_file="$out.scad"
  python3 -m "$module" scad > "$scad_file" 2> /dev/null

  echo "$scad_file"
}

function make_3d_printed {
  echo -n "$1 > "
  scad_file="$(make_scad "$1" "3d_printed/$2")"
  out_file="$(dirname "$scad_file")/$2.stl"
  echo "$out_file"
  openscad "$scad_file" -o "$out_file"
}

function make_laser_cut {
  echo -n "$1 > "
  scad_file="$(make_scad "$1" "laser_cut/$2")"
  out_file="$(dirname "$scad_file")/$2.dxf"
  echo "$out_file"
  openscad "$scad_file" -o "$out_file"
}

function make_machined {
  echo -n "$1 > "
  scad_file="$(make_scad "$1" "machined/$2")"
  out_file="$(dirname "$scad_file")/$2.stl"
  echo "$out_file"
  openscad "$scad_file" -o "$out_file"
}

function make_machined_2d {
  echo -n "$1 > "
  scad_file="$(make_scad "$1" "machined/$2")"
  out_file="$(dirname "$scad_file")/$2.dxf"
  echo "$out_file"
  openscad "$scad_file" -o "$out_file"
}

make_scad \
  "frame.assembly.assembly" \
  "assembly"

make_machined_2d \
  "frame.assembly.bumpers.front.bumper" \
  "front_bumper"

make_machined_2d \
  "frame.assembly.bumpers.rear.bumper" \
  "rear_bumper"

make_laser_cut \
  "frame.assembly.electronics_tray.tray" \
  "electronics_tray"

make_machined \
  "frame.assembly.front_axle.wheel_bushing" \
  "front_wheel_bushing"

make_machined_2d \
  "frame.assembly.motor.mount" \
  "motor_mount"

make_machined \
  "frame.assembly.rear_axle.brake_disc.mount" \
  "brake_disc_mount"

make_machined \
  "frame.assembly.rear_axle.drive_sprocket.mount" \
  "drive_sprocket_mount"

make_machined_2d \
  "frame.assembly.steering.column_mount.lower.mount" \
  "lower_steering_column_mount"

make_machined_2d \
  "frame.assembly.steering.column_mount.upper.mount" \
  "upper_steering_column_mount"

make_3d_printed \
  "frame.assembly.steering.instrument_panel.box" \
  "instrument_panel_box"

make_laser_cut \
  "frame.assembly.steering.instrument_panel.panel" \
  "instrument_panel"

make_3d_printed \
  "frame.assembly.steering.throttle.mount" \
  "throttle_mount"

make_3d_printed \
  "frame.assembly.steering.throttle.trigger" \
  "throttle_trigger"

make_machined_2d \
  "frame.assembly.steering.arm" \
  "steering_arm"

make_machined \
  "frame.assembly.steering.arm_mount" \
  "steering_column_arm_mount"

make_machined \
  "frame.assembly.steering.wheel_mount" \
  "steering_column_wheel_mount"

tree "$build_dir"
