#!/bin/bash

set -ex

# Create temporary build log and preview image files
log_file="$(mktemp).build.log"
image_file="$(mktemp).preview.png"

# Build the OpenSCAD global assembly
openscad -o "$image_file" --preview=- --hardwarnings assembly.scad 2> "$log_file"

# Output the contents of the build log
cat "$log_file"

# Check the build log for warnings and set a sensible exit code
result=0
if grep --silent 'WARNING' "$log_file"; then
  result=1
fi

# Remove temporary files
rm "$log_file" "$image_file"

exit $result
