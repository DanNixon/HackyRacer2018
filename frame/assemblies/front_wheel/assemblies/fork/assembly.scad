use <../../../../parts/box_section.scad>;

include <../../../../dimensions.scad>;

include <dimensions.scad>;

module FrontWheelForkAssembly()
{
  difference()
  {
    for (x = [-fork_spacing/2, fork_spacing/2])
    {
      translate([x, 0, -bottom_offset])
      {
        rotate([90, 0, 0])
        {
          BoxSection(box_section_outer, fork_length);
        }
      }
    }

    /* Axle holes */
    rotate([0, 90, 0])
    {
      cylinder(d=axle_diameter, h=500, center=true);
    }
  }

  translate([0, 0, fork_length - bottom_offset + box_section_outer[0]/2])
  {
    rotate([0, 90, 90])
    {
      BoxSection(box_section_outer, fork_spacing+box_section_outer[0], center=true, col="darkgreen");
    }
  }
}

FrontWheelForkAssembly();
