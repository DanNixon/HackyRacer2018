from frame.assembly.dimensions import inner
from frame.materials import box_section

tray_dimensions = (((inner * 2) + box_section.default_size[0]) - 5., 140.)
tray_thickness = 3.
