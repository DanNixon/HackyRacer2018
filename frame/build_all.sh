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
  echo "$1 > $2.stl"
  scad_file="$(make_scad "$1" "3d_printed/$2")"
  openscad "$scad_file" -o "$(dirname "$scad_file")/$2.stl"
}

function make_laser_cut {
  echo "$1 > $2.dxf"
  scad_file="$(make_scad "$1" "laser_cut/$2")"
  openscad "$scad_file" -o "$(dirname "$scad_file")/$2.dxf"
}

function make_machined {
  echo "$1 > $2.stl"
  scad_file="$(make_scad "$1" "machined/$2")"
  openscad "$scad_file" -o "$(dirname "$scad_file")/$2.stl"
}

make_machined \
  "frame.assembly.rear_axle.brake_disc.mount" \
  "brake_disc_mount"

make_machined \
  "frame.assembly.rear_axle.drive_sprocket.mount" \
  "drive_sprocket_mount"

tree "$build_dir"
