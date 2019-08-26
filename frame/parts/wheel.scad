module Wheel()
{
  $fn = 128;

  big = 250;
  thickness = 100;

  color("darkgray")
  {
    rotate([0, 90, 0])
    {
      difference()
      {
        union()
        {
          difference()
          {
            /* Outer dimensions */
            cylinder(d=290, h=thickness, center=true);

            /* Wheel */
            for(a = [0, 180])
            {
              rotate([0, a, 0])
              {
                translate([0, 0, -thickness / 2 - 0.1])
                {
                  cylinder(d=180, h=15);
                  cylinder(d=130, h=45);
                }
              }
            }

            /* Bolts */
            for(a = [0 : 360 / 5 : 359])
            {
              rotate([0, 0, a])
              {
                translate([0, 50, 0])
                {
                  cylinder(d=8, h=big, center=true);
                }
              }
            }
          }

          cylinder(h=thickness/2, d=38);
        }

        /* Shaft */
        cylinder(d=16, h=big, center=true);
      }
    }
  }
}

Wheel();
