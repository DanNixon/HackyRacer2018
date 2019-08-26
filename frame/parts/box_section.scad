module BoxSection(length, center, width=25, height=25, col="yellow")
{
  translate(center ? [0, 0, 0] : -[width/2, 0, height/2])
  {
    color(col)
    {
      cube([width, length, height], center=center);
    }
  }
}
