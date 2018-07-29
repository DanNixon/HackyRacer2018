include <config.scad>;

module RoundedRect(dimensions, radius=10)
{
  d = radius * 2;

  minkowski()
  {
    square(dimensions - [d, d], center=true);
    circle(d=d);
  }
}

module PlaceMountingHoles(centres, diameter)
{
  lx = centres[0] / 2;
  ly = centres[1] / 2;

  for (x = [-lx, lx])
  {
    for (y = [-ly, ly])
    {
      translate([x, y])
      {
        circle(d=diameter);
      }
    }
  }
}

module Plate()
{
  difference()
  {
    RoundedRect(plate_dimensions);

    PlaceMountingHoles(plate_mounting_hole_centres, plate_mounting_hole_diameter);

    translate(vesc_offset)
    {
      PlaceMountingHoles(vesc_mounting_hole_centres, vesc_mounting_hole_diameter);
    }
  }
}

Plate();
