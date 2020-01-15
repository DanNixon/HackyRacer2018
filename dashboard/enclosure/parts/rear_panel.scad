use <cable_entry.scad>
use <usb_breakout.scad>
use <gps_board.scad>

include <../common.scad>

module RearPanel()
{
  difference()
  {
    PanelProjection();

    translate(usb_breakout_position)
    {
      UsbBreakoutHoles();
    }

    translate(cable_entry_position)
    {
      CableEntryCableTies();
    }

    translate(gps_board_position)
    {
      GpsBoardHoles();
    }
  }
}

RearPanel();
