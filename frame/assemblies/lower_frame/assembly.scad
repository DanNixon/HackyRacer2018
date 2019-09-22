use <../../parts/box_section.scad>;

include <../../dimensions.scad>;

include <dimensions.scad>;

module LowerFrameAssembly()
{
  for (x = [-outer, outer])
  {
    translate([x, 0, 0])
    {
      BoxSection(outer_length, outer=box_section_outer, center=false);
    }
  }

  for (x = [-inner, inner])
  {
    translate([x, 0, 0])
    {
      BoxSection(inner_length, outer=box_section_outer, center=false);
    }
  }

  translate([0, inner_length + box_section_outer[0] / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(inner * 2 + box_section_outer[0], outer=box_section_outer, center=true, col="darkgreen");
    }
  }

  translate([0, outer_length + box_section_outer[0] / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(inner * 2 - box_section_outer[0], outer=box_section_outer, center=true, col="darkgreen");

      for (a = [0, 180])
      {
        rotate([0, 0, a])
        {
          translate([0, -outer - box_section_outer[0] / 2, 0])
          {
            BoxSection(outer - inner, outer=box_section_outer, center=false, col="lime");
          }
        }
      }
    }
  }

  translate([0, -box_section_outer[0] / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(outer * 2 + box_section_outer[0], outer=box_section_outer, center=true, col="darkgreen");
    }
  }

  /* Floor panel */
  translate([-inner-box_section_outer[0]/2, -box_section_outer[0], -(box_section_outer[1] + plate_thickness) / 2])
  {
    color("grey")
    {
      cube([inner * 2 + box_section_outer[0], inner_length + 2*box_section_outer[0], plate_thickness]);
    }
  }
}

LowerFrameAssembly();
