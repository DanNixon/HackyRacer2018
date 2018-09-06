use <screen_cutaway.scad>
include <config.scad>

module CaseDisplayMount()
{
  difference()
  {
    union()
    {
      cube([screen_mount_hole_size[0] + 4, screen_mount_hole_size[1] + 4, top_panel_thickness], center=true);

      translate([0, 0, top_panel_thickness])
      {
        cube(screen_mount_hole_size - [1, 1, 0], center=true);
      }
    }

    translate([0, 0, 6])
    {
      rotate([0, 180, 180])
      {
        ScreenCutaway(board_size=[60, 98]);
      }
    }
  }
}

CaseDisplayMount();
