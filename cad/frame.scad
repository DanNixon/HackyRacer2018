use <wheel.scad>;

module BoxSection(length)
{
  cube([25, length, 25], center=true);
}

main_width = 500;

rotate([0, 90, 0])
{
  /* Axle */
  color("red")
  {
    $fn = 64;
    cylinder(d=16, h=main_width + 150, center=true);
  }

  /* Break disc */
  translate([0, 0, 220])
  {
    color("green")
    {
      $fn = 64;
      cylinder(d=160, h=5, center=true);
    }
  }

  /* Drive sprocket */
  translate([0, 0, -220])
  {
    color("orange")
    {
      $fn = 64;
      cylinder(d=180, h=5, center=true);
    }
  }
}

/* Wheels */
for (a = [0, 180])
{
  rotate([0, 0, a])
  {
    translate([-(main_width + 100) / 2, 0, 0])
    {
      color("darkgrey")
      {
        Wheel();
      }
    }
  }
}

translate([0, 50, -20])
{
  translate([-190, 0, 0])
    BoxSection(500);

  translate([0, 0, 0])
    BoxSection(500);

  translate([190, 0, 0])
    BoxSection(500);
}
