height = 85;
upper_width = 135;
lower_width = 163;

panel_thickness = 1.5;
top_panel_thickness = 2;
wall_thickness = 2;

outer_bar_diameter = 22;
inner_rod_diameter = 15;

dwt = wall_thickness / 2;
dy = height / 2;
dx_upper = (upper_width + wall_thickness) / 2;
dx_lower = (lower_width +wall_thickness) / 2;
dx_inner_rod = inner_rod_diameter / 2;

p_ulo = [-dx_upper, dy];
p_uli = [-dx_upper+outer_bar_diameter+dwt, dy];
p_uml = [-dx_inner_rod-dwt, dy];
p_umr = [dx_inner_rod+dwt, dy];
p_uri = [dx_upper-outer_bar_diameter-dwt, dy];
p_uro = [dx_upper, dy];

p_llo = [-dx_lower, -dy];
p_lli = [-dx_lower+outer_bar_diameter+dwt, -dy];
p_lml = [-dx_inner_rod-dwt, -dy];
p_lmr = [dx_inner_rod+dwt, -dy];
p_lri = [dx_lower-outer_bar_diameter-dwt, -dy];
p_lro = [dx_lower, -dy];

p_screws = [
  [p_ulo[0]-2, dy-2],
  [p_uml[0]-2, dy-2],
  [p_umr[0]+2, dy-2],
  [p_uro[0]+2, dy-2],
  [p_llo[0]-2, -dy+2],
  [p_lli[0]+2.5, -dy+2],
  [p_lri[0]-2.5, -dy+2],
  [p_lro[0]+2, -dy+2]
];

usb_board_pos = [-22, 36.5, 0];
can_board_position = [-40, 5, 0];
amplifier_board_pos = [-41, -26, 0];
teensy_board_pos = [-19, -10, 0];
bec_module_pos = [25, 0, 0];

mount_screw_diameter = 2.9;
upper_mount_screw_diameter = 3.4;
mount_screw_outer = 6;

small_screw_diameter = 2.1;

screen_mount_hole_size = [65, 105, 4];
screen_angle = 20;
