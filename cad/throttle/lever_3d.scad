use <lever.scad>;
include <config.scad>;

module Lever3D()
{
  linear_extrude(lever_thickness, center=true)
  {
    Lever();
  }
}

Lever3D();
