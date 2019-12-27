import solid as sp

from frame.utils import entrypoint

from . import panel
from .dimensions import panel_thickness, switch_diameter, cherry_mx_cutout


def projection():
    x1 = -60.
    x2 = -80.

    xm = x1 + ((x2 - x1) / 2.)

    p = panel.projection(((x1, -60), (x1, 60), (x2, -60), (x2, 60)))

    horn_button = sp.translate((xm, 40))(
        sp.square(cherry_mx_cutout, center=True)
    )

    headlight_button = sp.translate((xm, 10))(
        sp.square(cherry_mx_cutout, center=True)
    )

    light_switch = sp.translate((xm, -20))(
        sp.circle(d=switch_diameter, segments=32)
    )

    return p - horn_button - headlight_button - light_switch


def volume():
    return sp.linear_extrude(panel_thickness)(projection())


if __name__ == '__main__':
    entrypoint.main(projection())
