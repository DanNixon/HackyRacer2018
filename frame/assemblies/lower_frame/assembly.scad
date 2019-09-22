use <../../parts/box_section.scad>;

include <../../dimensions.scad>;

include <dimensions.scad>;

module LowerFrameAssembly()
{
  for (x = [-outer, outer])
  {
    translate([x, 0, 0])
    {
      BoxSection(box_section_outer, outer_length, center=false);
    }
  }

  for (x = [-inner, inner])
  {
    translate([x, 0, 0])
    {
      BoxSection(box_section_outer, inner_length, center=false);
    }
  }

  translate([0, inner_length + box_section_outer[0] / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(box_section_outer, outer * 2 + box_section_outer[0], center=true, col="darkgreen");
    }
  }

  translate([0, outer_length + box_section_outer[0] / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(box_section_outer, inner * 2 - box_section_outer[0], center=true, col="darkgreen");

      for (a = [0, 180])
      {
        rotate([0, 0, a])
        {
          translate([0, -outer - box_section_outer[0] / 2, 0])
          {
            BoxSection(box_section_outer, outer - inner, center=false, col="lime");
          }
        }
      }
    }
  }

  translate([0, -box_section_outer[0] / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(box_section_outer, outer * 2 + box_section_outer[0], center=true, col="darkgreen");
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
