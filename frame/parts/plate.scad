module Plate(name, col, size, center)
{
  echo("plate", name, col, size);

  color(col)
  {
    cube(size, center=center);
  }
}
