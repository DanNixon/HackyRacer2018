use <RacerSprocket.scad>
include <common_config.scad>

RacerSprocket(
  chain_type = chain_type,
  teeth = 6,
  sprocket_round_dim = 25.5,
  key_screw_diameter = key_screw_diameter,
  key_screw_offset = 25,
  bore_diameter = bore_diameter,
  shaft_height = 30,
  shaft_height_outer = shaft_height_outer,
  shaft_diameter_inner = 9,
  shaft_diameter_outer = shaft_diameter_outer
);

cylinder(h=5, d=10);
