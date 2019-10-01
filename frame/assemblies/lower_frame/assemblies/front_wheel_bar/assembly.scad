use <../../../../primitives/box_section.scad>;

include <../../../../dimensions.scad>;

include <dimensions.scad>;

module FrontWheelBarAssembly()
{
  rotate([0, 0, 90])
  {
    BoxSection(
        name="lower_frame/front_wheel_x_bar",
        col="red",
        outer=box_section_outer,
        length=bar_length,
        center=true);
  }

  color("green")
  {
    for(a = [0, 180])
    {
      rotate([0, 0, a])
      {
        translate([(bar_length + bar_thickness) / 2, 0, 0])
        {
          cube([bar_thickness, box_section_outer[0], inner_height + (2 * bar_thickness)], center=true);

          for (z = [-inner_height/2 - bar_thickness, inner_height/2])
          {
            translate([0, -box_section_outer[0] / 2, z])
            {
              cube([inner_depth + bar_thickness, box_section_outer[0], bar_thickness]);
            }
          }
        }
      }
    }
  }
}

FrontWheelBarAssembly();
