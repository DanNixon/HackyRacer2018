use <parts/enclosure.scad>
use <parts/front_panel.scad>
use <parts/rear_panel.scad>
use <parts/teensy.scad>
use <parts/usb_breakout.scad>
use <parts/display.scad>
use <parts/gps_board.scad>
use <parts/can_board.scad>

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

  translate([0, 0, centre_section_depth - sheet_thickness])
  {
    Extrude("cyan")
    {
      translate(display_offset)
      {
        Display();
      }
    }
  }

  Enclosure();

  translate(teensy_position)
  {
    rotate([0, 0, 180])
    {
      Teensy35();
    }
  }

  translate(usb_breakout_position)
  {
    UsbBreakout();
  }

  translate(gps_board_position)
  {
    GpsBoard();
  }

  translate(can_board_position)
  {
    CanBoard();
  }

  translate([0, 0, (centre_section_depth / 2) - panel_distance])
  {
    Extrude("blue")
    {
      RearPanel();
    }
  }

  translate([0, 0, (centre_section_depth / 2) + panel_distance])
  {
    Extrude([1, 0, 0, 0.25])
    {
      FrontPanel();
    }
  }
}

Assembly(explode=10);
