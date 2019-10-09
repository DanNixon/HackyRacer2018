use <../../parts/wheel.scad>;

use <assemblies/brake_disc/assembly.scad>;
use <assemblies/drive_sprocket/assembly.scad>;

include <../../dimensions.scad>;

include <dimensions.scad>;

module RearAxleAssembly()
{
  rotate([0, 90, 0])
  {
    /* Axle */
    color("red")
    {
      $fn = 64;
      axle_length = wheel_centre_distance + 120;
      cylinder(d=axle_diameter, h=axle_length, center=true);
    }

    /* Drive sprocket */
    color("green")
    {
      translate([0, 0, sprocket_pos])
      {
        rotate([0, 180, 0])
        {
          DriveSprocketAssembly();
        }
      }
    }

    /* Brake disc */
    color("blue")
    {
      translate([0, 0, brake_disc_pos])
      {
        BrakeDiscAssembly();
      }
    }
  }

  /* Wheels */
  for (a = [0, 180])
  {
    rotate([0, 0, a])
    {
      translate([wheel_centre_distance / 2, 0, 0])
      {
        Wheel();
      }
    }
  }
}

RearAxleAssembly();
