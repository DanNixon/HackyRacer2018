use <../../primitives/assembly_instruction.scad>;
use <../../primitives/box_section.scad>;
use <../../primitives/plate.scad>;

include <../../dimensions.scad>;

include <dimensions.scad>;

module LowerFrameAssembly()
{
  for (x = [-outer, outer])
  {
    translate([x, 0, 0])
    {
      BoxSection(
          name="lower_frame/short_y_bar",
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
          name="lower_frame/long_y_bar",
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
            name="lower_frame/front_bumper_y_bar",
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
            name="lower_frame/front_bumper_x_bar",
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
          name="lower_frame/front_wheel_x_bar",
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
          name="lower_frame/inner_mid_x_bar",
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
                name="lower_frame/outer_mid_x_bar",
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
          name="lower_frame/rear_x_bar",
          col="magenta",
          outer=box_section_outer,
          length=outer * 2 + box_section_outer[0],
          center=true);
    }
  }

  /* Floor panel */
  translate([-inner-box_section_outer[0]/2, -box_section_outer[0], -(box_section_outer[1] + plate_thickness) / 2])
  {
    AssemblyInstruction(
        "lower_frame/floor_panel",
        "Clearence holes drilled into lower floor plate");

    AssemblyInstruction(
        "lower_frame/floor_panel",
        "Tap threads into lower frame box section");

    Plate(
        name="lower_frame/floor_panel",
        col="gray",
        size=[inner * 2 + box_section_outer[0], inner_length + 2*box_section_outer[0], plate_thickness],
        center=false);
  }
}

LowerFrameAssembly();
