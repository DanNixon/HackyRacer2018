import solid as sp

from frame.utils import bom, entrypoint, place_n_at_x_around

# This isn't an accurate representation of the steering wheel.
# The main plate section is not actually flat, but for design purposes that
# isn't overly important.

plate_thickness = 6.

mounting_hole_diameter = 6.

xu = 150.
yu = 60.

xd = 125.
yd = -60.

top_hand_grip_extra = 30.


def place_mounting_holes(obj):
    return place_n_at_x_around(3, 20, obj)


def projection():
    cu = 30.
    cd = -30.

    def arm(a, b):
        return sp.hull()(
            sp.translate(a)(sp.circle(d=20., segments=32)),
            sp.translate(b)(sp.circle(d=25., segments=32)),
        )

    return sp.union()(
        sp.square((75., 75.), center=True),
        arm((-xu, yu), (0, cu)),
        arm((xu, yu), (0, cu)),
        arm((-xd, yd), (0, cd)),
        arm((xd, yd), (0, cd)),
    ) - place_mounting_holes(sp.circle(d=mounting_hole_diameter))


@bom.part('Steering Wheel')
def volume():
    def handle_bar(points):
        hand_grip_diameter = 20.
        return sp.union()(
            [
                sp.hull()(
                    sp.translate(points[i])(
                        sp.sphere(d=hand_grip_diameter, segments=32)
                    ),
                    sp.translate(points[i + 1])(
                        sp.sphere(d=hand_grip_diameter, segments=32)
                    ),
                ) for i in range(len(points) - 1)
            ]
        )

    return sp.union()(
        sp.linear_extrude(plate_thickness, center=True)(projection()),
        handle_bar(((-xd, yd), (-xu, yu), (-xu, yu + top_hand_grip_extra))),
        handle_bar(((xd, yd), (xu, yu), (xu, yu + top_hand_grip_extra))),
    )


if __name__ == '__main__':
    entrypoint.main(volume())
