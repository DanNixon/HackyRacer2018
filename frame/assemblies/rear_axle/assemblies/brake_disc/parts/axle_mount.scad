include <../../../../../dimensions.scad>;

module AxleMount()
{
  difference()
  {
    union()
    {
      translate([0, 0, 5])
      {
        cylinder(d=38, h=5, center=true);
      }

      cylinder(d=60, h=10);

      cylinder(d=30, h=40);
    }

    /* Axle hole */
    cylinder(d=axle_diameter, h=100, center=true);
  }
}

AxleMount();
