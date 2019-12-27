import solid as sp

from frame.utils import entrypoint

from . import panel
from .dimensions import panel_thickness, switch_diameter, cherry_mx_cutout


def projection():
    p = panel.projection(((0, -50), (0, 50), (-50, -60), (-50, 60)))

    horn_button = sp.translate((-40, 40))(
        sp.square(cherry_mx_cutout, center=True)
    )

    headlight_button = sp.translate((-40, 20))(
        sp.square(cherry_mx_cutout, center=True)
    )

    light_switch = sp.translate((-40, 0))(
        sp.circle(d=switch_diameter, segments=32)
    )

    return p - horn_button - headlight_button - light_switch


def volume():
    return sp.linear_extrude(panel_thickness)(projection())


if __name__ == '__main__':
    entrypoint.main(projection())
