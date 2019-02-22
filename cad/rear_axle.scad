use <wheel.scad>;

main_width = 500;

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
