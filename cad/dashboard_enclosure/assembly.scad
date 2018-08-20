use <screen_cutaway.scad>

difference()
{
  linear_extrude(6)
  {
    square([80, 120], center=true);
  }

  translate([0, 0, -1])
  {
    ScreenCutaway(board_size=[60, 100]);
  }
}
