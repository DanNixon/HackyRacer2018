use <common.scad>
use <vesc.scad>
include <config.scad>

module RoundedRect(dimensions, radius=10)
{
  d = radius * 2;

  minkowski()
  {
    square(dimensions - [d, d], center=true);
    circle(d=d);
  }
}

module Plate()
{
  difference()
  {
    RoundedRect(plate_dimensions);

    PlaceAtCentres(plate_mounting_hole_centres)
    {
      circle(d=plate_mounting_hole_diameter);
    }

    translate(vesc_offset)
    {
      PlaceAtCentres(VescMountingHoleCentres())
      {
        circle(d=vesc_mounting_hole_diameter);
      }
    }
  }
}

Plate();
