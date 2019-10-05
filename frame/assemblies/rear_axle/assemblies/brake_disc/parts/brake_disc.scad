module BrakeDisc()
{
  $fn = 64;

  thickness = 2;

  difference()
  {
    cylinder(d=140, h=thickness, center=true);

    cylinder(d=38, h=thickness+1, center=true);

    for (a = [0 : 360 / 6: 359])
    {
      rotate([0, 0, a])
      {
        translate([24, 0, 0])
        {
          cylinder(d=6, h=thickness+1, center=true);
        }
      }
    }
  }
}

BrakeDisc();
