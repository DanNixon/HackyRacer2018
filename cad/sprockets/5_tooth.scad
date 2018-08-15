use <RacerSprocket.scad>
include <common_config.scad>

RacerSprocket(
  chain_type = chain_type,
  teeth = 5,
  sprocket_round_dim = 22,
  key_screw_diameter = key_screw_diameter,
  key_screw_offset = 33,
  bore_diameter = bore_diameter,
  shaft_height = 38,
  shaft_height_outer = shaft_height_outer,
  shaft_diameter_inner = 8,
  shaft_diameter_outer = shaft_diameter_outer
);

cylinder(h=5, d=10, $fn=32);
