use <common.scad>

module MoxyBoard()
{
  Board()
  {
    /* TODO */

    translate([-75, 10])
    {
      TitleText("200");
    }

    translate([-75, -10])
    {
      TitleText("CARTRIDGES");
    }
  }
}

MoxyBoard();
