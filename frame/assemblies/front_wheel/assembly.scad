use <../../parts/box_section.scad>;
use <../../parts/wheel.scad>;

include <../../dimensions.scad>;

include <dimensions.scad>;

module FrontWheelAssembly()
{
  Wheel();

  for (x = [-fork_spacing/2, fork_spacing/2])
  {
    translate([x, 0, -bottom_offset])
    {
      rotate([90, 0, 0])
      {
        BoxSection(fork_length, outer=box_section_outer);
      }
    }
  }

  translate([0, 0, fork_length - bottom_offset + box_section_outer[0]/2])
  {
    rotate([0, 90, 90])
    {
      BoxSection(fork_spacing+box_section_outer[0], outer=box_section_outer, center=true, col="darkgreen");
    }
  }
}

FrontWheelAssembly();
