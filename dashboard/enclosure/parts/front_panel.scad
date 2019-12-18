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
}

FrontPanel();
