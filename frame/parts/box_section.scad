module BoxSection(length, center, width=25, height=25)
{
  translate(center ? [0, 0, 0] : -[width/2, 0, height/2])
  {
    cube([width, length, height], center=center);
  }
}
