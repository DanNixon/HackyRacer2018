import solid as sp
import solid.utils as spu

from frame.utils import place_at_centres, place_n_at_x_around

body_diameter = 108
body_length = 140

mounting_hole_centres = 90
mounting_hole_diameter = 5

shaft_diameter = 12
shaft_length = 30

sprocket_diameter = 30
sprocket_pos = 16

shaft_surround_diam = 22

vent_holes_centres = 65
vent_holes_diameter = 10


def motor():
    mounting_holes = spu.down(1)(
        place_at_centres(
            [mounting_hole_centres, 0],
            sp.cylinder(d=mounting_hole_diameter, h=body_length + 2)
        )
    )

    body = sp.color('orange')(
        sp.rotate(
            [0, 180, 0]
        )(sp.cylinder(d=body_diameter, h=body_length) - mounting_holes, )
    )

    shaft = sp.color('black')(sp.cylinder(d=shaft_diameter, h=shaft_length), )

    sprocket = sp.color('cyan')(
        spu.up(sprocket_pos)
        (sp.cylinder(d=sprocket_diameter, h=5, center=True), )
    )

    return sp.union()(
        body,
        shaft,
        sprocket,
    )


def mountable_face():
    outer = sp.circle(d=body_diameter)

    shaft_cutout = sp.circle(d=shaft_surround_diam)

    mounting_holes = place_at_centres(
        [mounting_hole_centres, 0], sp.circle(d=mounting_hole_diameter)
    )

    vent_holes = place_n_at_x_around(8, vent_holes_centres / 2., sp.circle(d=vent_holes_diameter))

    return outer - shaft_cutout - mounting_holes - vent_holes


if __name__ == '__main__':
    print(sp.scad_render(motor()))
    # print(sp.scad_render(mountable_face()))
