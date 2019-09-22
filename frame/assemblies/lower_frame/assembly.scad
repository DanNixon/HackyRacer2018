use <../../parts/box_section.scad>;

include <../../dimensions.scad>;

include <dimensions.scad>;

module LowerFrameAssembly()
{
  for (x = [-outer, outer])
  {
    translate([x, 0, 0])
    {
      BoxSection(outer_length, false);
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

  /* Floor panel */
  translate([-inner-box_section_outer/2, -box_section_outer, -(box_section_outer + plate_thickness) / 2])
  {
    color("grey")
    {
      cube([inner * 2 + box_section_outer, inner_length + 2*box_section_outer, plate_thickness]);
    }
  }
}

LowerFrameAssembly();
