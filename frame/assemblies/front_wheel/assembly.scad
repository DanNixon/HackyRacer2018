use <../../parts/wheel.scad>;

use <assemblies/fork/assembly.scad>;

include <../../dimensions.scad>;

module FrontWheelAssembly()
{
  Wheel();

  FrontWheelForkAssembly();

  /* Axle */
  color("red")
  {
    rotate([0, 90, 0])
    {
      cylinder(d=axle_diameter, h=200, center=true);
    }
  }
}

FrontWheelAssembly();
