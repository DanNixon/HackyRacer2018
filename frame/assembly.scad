use <subassemblies/rear_axle.scad>;

module BoxSection(length)
{
  cube([25, length, 25], center=true);
}

translate([0, 0, 25])
{
  RearAxle(16, 600, -180, 180);
}

translate([-210, 0, 0])
  BoxSection(500);

translate([-120, 0, 0])
  BoxSection(500);

translate([120, 0, 0])
  BoxSection(500);

translate([210, 0, 0])
  BoxSection(500);

rotate([0, 0, 90])
{
  translate([-250, 0, 0])
  {
    BoxSection(500);
  }
}
