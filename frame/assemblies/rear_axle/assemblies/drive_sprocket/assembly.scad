use <parts/axle_mount.scad>;
use <parts/drive_sprocket.scad>;

module DriveSprocketAssembly()
{
  color("red")
  {
    DriveSprocket();
  }

  color("green")
  {
    translate([0, 0, 2])
    {
      AxleMount();
    }
  }
}

DriveSprocketAssembly();
