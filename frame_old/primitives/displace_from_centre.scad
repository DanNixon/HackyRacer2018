module DisplaceFromCentre(name, x_positions=[0], y_positions=[0])
{
  for(x = x_positions)
  {
    for(y = y_positions)
    {
      p = [x, y];
      translate(p)
      {
        echo("displace_from_centre", name, p);
        children();
      }
    }
  }
}
