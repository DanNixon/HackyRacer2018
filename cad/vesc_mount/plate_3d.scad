use <plate.scad>
include <config.scad>

module Plate3D()
{
  linear_extrude(plate_thickness)
  {
    Plate();
  }
}

Plate3D();
