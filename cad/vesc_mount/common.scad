module PlaceAtCentres(centres)
{
  lx = centres[0] / 2;
  ly = centres[1] / 2;

  for (x = [-lx, lx])
  {
    for (y = [-ly, ly])
    {
      translate([x, y])
      {
        children();
      }
    }
  }
}
