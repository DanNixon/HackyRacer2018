use <parts/axle_mount.scad>
use <parts/brake_disc.scad>

module BrakeDiscAssembly()
{
  color("red")
  {
    BrakeDisc();
  }

  color("green")
  {
    translate([0, 0, 1])
    {
      AxleMount();
    }
  }
}

BrakeDiscAssembly();
