use <common.scad>
include <config.scad>

module CaseUpper()
{
  difference()
  {
    union()
    {
      linear_extrude(top_panel_thickness)
      {
        PointHull([p_ulo, p_uro, p_llo, p_lro]);
      }

      for(p=p_screws)
      {
        translate(p)
        {
          cylinder(h=top_panel_thickness, d=mount_screw_outer, $fn=32);
        }
      }
    }

    translate([0, 0, -1])
    {
      for(p=p_screws)
      {
        translate(p)
        {
          cylinder(h=top_panel_thickness+2, d=upper_mount_screw_diameter, $fn=32);
        }
      }
    }

    /* Cable routing hole */
    translate([-22, -15, 0])
    {
      cube([18, 25, 10], center=true);
    }

    /* Top of screen cutout */
    translate([0, 18, 0])
    {
      cube([60, 20, 10], center=true);
    }
  }

  difference()
  {
    intersection()
    {
      translate([0, 30, 0])
      {
        DisplayMountPart(width=72, length=115, angle=screen_angle, wall=4);
      }

      linear_extrude(height=100)
      {
        square([100, 200], center=true);
      }
    }

    rotate([-screen_angle, 0, 0])
    {
      translate([0, -25, 15])
      {
        cube(screen_mount_hole_size + [0, 0, 4], center=true);
      }
    }
  }

  /* Side braces */
  for(x=[-44, 44])
  {
    translate([x, -11, 4])
    {
      cube([18, 65, 6], center=true);
    }
  }
}

CaseUpper();
