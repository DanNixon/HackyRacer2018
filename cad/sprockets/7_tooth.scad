use <RacerSprocket.scad>
include <common_config.scad>

RacerSprocket(
  chain_type = chain_type,
  teeth = 7,
  sprocket_round_dim = 30,
  key_screw_diameter = key_screw_diameter,
  key_screw_offset = 20,
  bore_diameter = bore_diameter,
  shaft_height = 25,
  shaft_height_outer = shaft_height_outer,
  shaft_diameter_inner = 13,
  shaft_diameter_outer = shaft_diameter_outer
);