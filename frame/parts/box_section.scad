module BoxSection(name, col, outer, length, center)
{
  echo("box_section", name, col, "outer=", outer, "length=", length);

  translate(center ? [0, 0, 0] : -[outer[0]/2, 0, outer[1]/2])
  {
    color(col)
    {
      cube([outer[0], length, outer[1]], center=center);
    }
  }
}
