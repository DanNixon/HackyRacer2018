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

  translate([0, -box_section_outer[0] / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(box_section_outer, outer * 2 + box_section_outer[0], center=true, col="darkgreen");
    }
  }

  translate([0, inner_length + box_section_outer[0] / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(box_section_outer, outer * 2 - box_section_outer[0], center=true, col="darkgreen");
    }
  }

  magic_1 = 220;

  translate([0, outer_length - box_section_outer[0] / 2, 0])
  {
    translate([0, 0, magic_1])
    {
      rotate([0, 0, 90])
      {
        BoxSection(box_section_outer, outer * 2 + box_section_outer[0], center=true, col="darkgreen");
      }
    }

    for (x = [-outer, outer])
    {
      translate([x, 0, box_section_outer[0]/2])
      {
        rotate([90, 0, 0])
        {
          BoxSection(box_section_outer, magic_1 - box_section_outer[0], center=false, col="blue");
        }
      }
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
