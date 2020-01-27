use <display.scad>

include <../common.scad>

module FrontPanel()
{
  difference()
  {
    PanelProjection();

    translate(display_offset)
    {
      DisplayMountingHoles();
    }
  }

  translate([0, outer_size[1] / 2])
  {
    MountingTab(hole_diameter=4.1, hole_centres=50, outer_radius=10, hole_offset=15);
  }
}

FrontPanel();
