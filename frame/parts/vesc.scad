module Vesc()
{
  $fn = 64;

  body_dimensions = [45, 85, 23];
  mounting_hole_centres = [39, 79];

  difference()
  {
    translate([0, 0, body_dimensions[2]/2])
    {
      cube(body_dimensions, center=true);
    }

    for(x=[-mounting_hole_centres[0]/2, mounting_hole_centres[0]/2])
    {
      for(y=[-mounting_hole_centres[1]/2, mounting_hole_centres[1]/2])
      {
        translate([x, y, -1])
        {
          cylinder(d=4, h=body_dimensions[2]+2);
        }
      }
    }
  }
}

Vesc();
