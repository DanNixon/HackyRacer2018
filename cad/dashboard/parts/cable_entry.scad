module CableEntryHole()
{
  width = 6;
  height = 3;

  translate([-25, -width / 2, -1])
  {
    cube([50, width, height + 1]);
  }
}

module CableEntryCableTies()
{
  centres = 8;
  hole_diameter = 3;

  for(y = [-centres / 2, centres / 2])
  {
    translate([0, y, 0])
    {
      circle(d=hole_diameter, $fn=16);
    }
  }
}
