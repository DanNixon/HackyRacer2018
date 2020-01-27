include <../common.scad>

module DisplayMountingHoles()
{
  PlaceAtCentres([76, 44.5])
  {
    circle(d=3.2, $fn=32);
  }
}

module Display()
{
  difference()
  {
    translate([2, 0])
    {
      square([85, 50], center=true);
    }

    DisplayMountingHoles();
  }
}

Display();
