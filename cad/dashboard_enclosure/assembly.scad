use <case_lower.scad>
use <case_upper.scad>
use <case_display.scad>

CaseLower(show_parts=false);

translate([0, 0, 30])
{
  CaseUpper();

  translate([0, -14, 30])
  {
    rotate([160, 0, 0])
    {
      CaseDisplayMount();
    }
  }
}
