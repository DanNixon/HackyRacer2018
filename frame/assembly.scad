use <parts/motor.scad>;

use <assemblies/front_wheel/assembly.scad>;
use <assemblies/lower_frame/assembly.scad>;
use <assemblies/rear_axle/assembly.scad>;
use <assemblies/seat_mount/assembly.scad>;

include <dimensions.scad>

front_wheel_angle = 0; // [-90:0.5:90]

translate([0, 810, 0])
{
  rotate([0, 0, front_wheel_angle])
  {
    FrontWheelAssembly();
  }
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
