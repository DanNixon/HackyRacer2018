use <../../parts/box_section.scad>;

include <../../dimensions.scad>;

include <dimensions.scad>;

module LowerFrameAssembly()
{
  for (x = [-outer, outer])
  {
    translate([x, 0, 0])
    {
      BoxSection(
          name="lower_frame/section_a",
          col="red",
          outer=box_section_outer,
          length=outer_length,
          center=false);
    }
  }

  for (x = [-inner, inner])
  {
    translate([x, 0, 0])
    {
      BoxSection(
          name="lower_frame/section_b",
          col="green",
          outer=box_section_outer,
          length=inner_length,
          center=false);
    }
  }

  /* Front bumper */
  translate([0, inner_length + box_section_outer[0] / 2, 0])
  {
    for (x = [-inner, inner])
    {
      translate([x, box_section_outer[0]/2, 0])
      {
        BoxSection(
            name="lower_frame/section_c",
            col="blue",
            outer=box_section_outer,
            length=front_bumper_depth - box_section_outer[0],
            center=false);
      }
    }

    translate([0, front_bumper_depth, 0])
    {
      rotate([0, 0, 90])
      {
        BoxSection(
            name="lower_frame/section_d",
            col="orange",
            outer=box_section_outer,
            length=inner * 2 + box_section_outer[0],
            center=true);
      }
    }
  }

  translate([0, inner_length + box_section_outer[0] / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(
          name="lower_frame/section_e",
          col="purple",
          outer=box_section_outer,
          length=outer * 2 + box_section_outer[0],
          center=true);
    }
  }

  translate([0, outer_length + box_section_outer[0] / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(
          name="lower_frame/section_f",
          col="cyan",
          outer=box_section_outer,
          length=inner * 2 - box_section_outer[0],
          center=true);

      for (a = [0, 180])
      {
        rotate([0, 0, a])
        {
          translate([0, -outer - box_section_outer[0] / 2, 0])
          {
            BoxSection(
                name="lower_frame/section_g",
                col="yellow",
                outer=box_section_outer,
                length=outer - inner,
                center=false);
          }
        }
      }
    }
  }

  translate([0, -box_section_outer[0] / 2, 0])
  {
    rotate([0, 0, 90])
    {
      BoxSection(
          name="lower_frame/section_h",
          col="magenta",
          outer=box_section_outer,
          length=outer * 2 + box_section_outer[0],
          center=true);
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
