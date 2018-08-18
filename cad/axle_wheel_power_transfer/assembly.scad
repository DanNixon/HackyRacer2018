use <components.scad>

difference()
{
  union()
  {
    WheelInterface(
        diameter_inner = 46,
        diameter_mid = 65,
        diameter_outer = 85,
        depth = 32,
        depth_lower = 13,
        depth_upper = 11,
        fin_thickness = 4,
        fin_offset = 4
      );

    AxleMount(
        diameter_outer = 85,
        diameter_inner = 60,
        depth = 20,
        depth_mid = 5,
        axle_bore = 12.5
      );
  }

  translate([0, 0, 9])
  {
    KeyScrewHole(
        key_screw_diameter = 7.75,
        key_screw_thread_length = 16,
        key_screw_head_diameter = 16
      );
  }
}
