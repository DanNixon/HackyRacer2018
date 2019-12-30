import solid as sp

from frame.utils import entrypoint

from .common import outer_projection
from .dimensions import panel_thickness, switch_diameter, cherry_mx_cutout


def projection():
    p = outer_projection()

    horn_button = sp.translate((-20, 15))(
        sp.square(cherry_mx_cutout, center=True)
    )

    headlight_button = sp.translate((-20, -15))(
        sp.square(cherry_mx_cutout, center=True)
    )

    light_switch = sp.translate((0, -15))(
        sp.circle(d=switch_diameter, segments=32)
    )

    gear_select_switch = sp.translate((20, 15))(
        sp.circle(d=switch_diameter, segments=32)
    )

    display_button = sp.translate((20, -15))(
        sp.square(cherry_mx_cutout, center=True)
    )

    return p - horn_button - headlight_button - light_switch - gear_select_switch - display_button


def volume():
    return sp.linear_extrude(panel_thickness)(projection())


if __name__ == '__main__':
    entrypoint.main(projection())
