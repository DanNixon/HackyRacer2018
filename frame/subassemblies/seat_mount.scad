use <../parts/box_section.scad>;

module SeatMount(width, depth)
{
  for (y = [-depth/2, depth/2])
  {
    translate([0, y, 0])
    {
      rotate([0, 0, 90])
      {
        BoxSection(width + 25, true, col="darkgreen");
      }
    }
  }

  for (x = [-width/2, width/2])
  {
    translate([x, 0, 0])
    {
      BoxSection(depth-25.0, true);
    }
  }
}
