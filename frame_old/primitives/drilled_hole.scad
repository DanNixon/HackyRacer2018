module DrilledHole(name, d)
{
  echo("drilled_hole", name, "diameter=", d);
  cylinder(h=1000, d=d, center=true);
}
