use <parts/motor.scad>;

use <assemblies/front_wheel/assembly.scad>;
use <assemblies/lower_frame/assembly.scad>;
use <assemblies/rear_axle/assembly.scad>;
use <assemblies/seat_mount/assembly.scad>;

include <dimensions.scad>

echo("All dimensions in millimetre.");

color("red")
{
  LowerFrameAssembly();
}

translate([0, 180, 160])
{
  color("green")
  {
    SeatMountAssembly();
  }
}

translate([0, 180, 25])
{
  color("blue")
  {
    RearAxleAssembly();
  }
}

translate([0, inner_length + box_section_outer[0]/2, 0])
{
  for(a = [0, 180])
  {
    rotate([0, 0, a])
    {
      translate([wheel_centre_distance/2-100, 0, 0])
      {
        color("cyan")
        {
          FrontWheelAssembly();
        }
      }
    }
  }
}

translate([-130, 300, 75])
{
  color("magenta")
  {
    Motor();
  }
}
