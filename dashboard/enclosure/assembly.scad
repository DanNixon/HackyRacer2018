use <parts/enclosure.scad>
use <parts/front_panel.scad>
use <parts/rear_panel.scad>

include <common.scad>

module Extrude(c)
{
  color(c)
  {
    linear_extrude(sheet_thickness, center=true)
    {
      children();
    }
  }
}

module Assembly(explode)
{
  panel_distance = explode + (centre_section_depth + sheet_thickness) / 2;

  translate([0, 0, (centre_section_depth / 2) + panel_distance])
  {
    Extrude("red")
    {
      FrontPanel();
    }
  }

  Enclosure();

  translate([0, 0, (centre_section_depth / 2) - panel_distance])
  {
    Extrude("blue")
    {
      RearPanel();
    }
  }
}

Assembly(explode=10);
