include <../dimensions.scad>;

module DriveSprocket()
{
  $fn = 64;

  thickness = 3;

  difference()
  {
    cylinder(d=sprocket_diameter, h=thickness, center=true);

    cylinder(d=26, h=thickness+1, center=true);

    for (a = [0 : 360 / 3: 359])
    {
      rotate([0, 0, a])
      {
        translate([20, 0, 0])
        {
          cylinder(d=6, h=thickness+1, center=true);
        }
      }
    }
  }
}

DriveSprocket();
