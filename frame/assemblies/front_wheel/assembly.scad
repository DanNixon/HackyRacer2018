use <../../parts/wheel.scad>;

include <../../dimensions.scad>;

include <dimensions.scad>;

module FrontWheelAssembly()
{
  translate([100, 0, 0])
  {
    color("red")
    {
      Wheel();
    }
  }

  color("green")
  {
    hull()
    {
      $fn = 64;

      cylinder(h=magic_1, r=magic_2, center=true);

      translate([magic_4, 0, 0])
      {
        cylinder(h=magic_1, r=magic_3, center=true);
      }
    }
  }

  color("blue")
  {
    rotate([0, 90, 0])
    {
      cylinder(d=axle_diameter, h=160);
    }
  }
}

FrontWheelAssembly();
