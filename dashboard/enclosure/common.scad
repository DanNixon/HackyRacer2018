include <config.scad>

module PointHull(points)
{
  hull()
  {
    for(p=points)
    {
      translate(p)
      {
        circle(d=wall_thickness, $fn=32);
      }
    }
  }
}

module DisplayMountPart(width, length, angle, wall)
{
  module Segment(d, l)
  {
    hull()
    {
      circle(d=d);

      translate([l-d, 0])
      {
        circle(d=d);
      }

      rotate([0, 0, angle])
      {
        translate([l-d, 0])
        {
          circle(d=d);
        }
      }
    }
  }

  rotate([90, 0, -90])
  {
    linear_extrude(height=width, center=true)
    {
      difference()
      {
        Segment(10, length);
        Segment(10 - (2 * wall), length - (2 * wall));
      }
    }

    dx = (width - wall) / 2;
    for(x=[-dx, dx])
    {
      translate([0, 0, x])
      {
        linear_extrude(height=wall, center=true)
        {
          Segment(10, length);
        }
      }
    }
  }
}
