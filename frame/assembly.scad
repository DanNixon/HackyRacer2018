use <parts/box_section.scad>;
use <parts/motor.scad>
use <subassemblies/rear_axle.scad>;

translate([0, 0, 25])
{
  RearAxle(16, 600, -180, 180);
}

translate([-130, 120, 75])
{
  Motor();
}

translate([0, -180, 0])
{
  outer = 210;
  inner = 120;

  for (x = [-outer, outer])
  {
    translate([x, 0, 0])
    {
      BoxSection(500, false);
    }
  }

  for (x = [-inner, inner])
  {
    translate([x, 0, 0])
    {
      BoxSection(500, false);
    }
  }

  translate([0, -12.5, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(outer * 2 + 25, true);
    }
  }
}
