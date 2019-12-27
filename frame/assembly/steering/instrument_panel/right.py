import solid as sp

from frame.utils import entrypoint

from . import panel
from .dimensions import panel_thickness, switch_diameter, cherry_mx_cutout


def projection():
    p = panel.projection(((0, -50), (0, 50), (40, -55), (50, 60)))

    gear_select_switch = sp.translate(
        (40, 40)
    )(sp.circle(d=switch_diameter, segments=32), )

    display_button = sp.translate((30, 10)
                                 )(sp.square(cherry_mx_cutout, center=True), )

    return p - gear_select_switch - display_button


def volume():
    return sp.linear_extrude(panel_thickness)(projection())


if __name__ == '__main__':
    entrypoint.main(projection())
