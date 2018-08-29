module TitleText(t)
{
  text(t, size=20, halign="left", valign="center", font="Octin Prison:style=Regular");
}

module Board()
{
  board_dimensions = [150, 45];

  linear_extrude(height=0.8)
  {
    difference()
    {
      square(board_dimensions, center=true);
      children();
    }
  }

  linear_extrude(height=1.5)
  {
    difference()
    {
      square(board_dimensions, center=true);
      square(board_dimensions - [2, 2], center=true);
    }
  }
}
