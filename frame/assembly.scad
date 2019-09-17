use <parts/motor.scad>;
use <parts/wheel.scad>;

use <assemblies/lower_frame/assembly.scad>;
use <assemblies/rear_axle/assembly.scad>;
use <assemblies/seat_mount/assembly.scad>;

include <dimensions.scad>

translate([0, 900, 0])
{
  Wheel();
}

translate([0, -180, 0])
{
  LowerFrameAssembly();
}

translate([0, 0, 160])
{
  SeatMountAssembly();
}

translate([0, 0, 25])
{
  RearAxleAssembly();
}

translate([-130, 120, 75])
{
  Motor();
}
