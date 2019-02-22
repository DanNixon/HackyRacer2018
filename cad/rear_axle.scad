use <wheel.scad>;

main_width = 600;

rotate([0, 90, 0])
{
  color("blue")
  {
    cube([20, 20, main_width], center=true);
  }

  color("red")
  {
    $fn = 64;
    cylinder(d=16, h=main_width+150, center=true);
  }

  dz = (main_width / 2) - 50;
  for (z = [-dz, dz])
  {
    x = 50;

    rotate([0, 0, 150])
    {
      translate([-x/2, -x/2, z])
      {
        cube([x, 250, 5]);
      }
    }
  }
}

for (a = [0, 180])
{
  rotate([0, 0, a])
  {
    translate([-(main_width + 104) / 2, 0, 0])
    {
      color("darkgrey")
      {
        Wheel();
      }
    }
  }
}
