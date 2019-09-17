use <parts/box_section.scad>;
use <parts/motor.scad>
use <parts/wheel.scad>;

use <assemblies/rear_axle/assembly.scad>;
use <assemblies/seat_mount/assembly.scad>;

include <dimensions.scad>

translate([0, 0, 25])
{
  RearAxleAssembly(16, 600, -180, 180);
}

translate([-130, 120, 75])
{
  Motor();
}

/* Front wheel */
translate([0, 900, 0])
{
  Wheel();
}

translate([0, -180, 0])
{
  outer_length = 500;
  inner_length = 800;

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
      BoxSection(inner_length, false);
    }
  }

  translate([0, inner_length + box_section_outer / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(inner * 2 + box_section_outer, true, col="darkgreen");
    }
  }

  translate([0, outer_length + box_section_outer / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(inner * 2 - box_section_outer, true, col="darkgreen");

      for (a = [0, 180])
      {
        rotate([0, 0, a])
        {
          translate([0, -outer - box_section_outer / 2, 0])
          {
            BoxSection(outer - inner, false, col="lime");
          }
        }
      }
    }
  }

  translate([0, -box_section_outer / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(outer * 2 + box_section_outer, true, col="darkgreen");
    }
  }
}

/* Floor panel */
translate([0, 220, -(box_section_outer + plate_thickness) / 2])
{
  color("grey")
  {
    cube([inner * 2 + box_section_outer, 820 + box_section_outer, plate_thickness], center=true);
  }
}

translate([0, 0, 160])
{
  SeatMountAssembly(outer*2, 280);
}
