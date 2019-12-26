import solid as sp

from frame.utils import bom, entrypoint, place_n_at_x_around

# This isn't an accurate representation of the steering wheel.
# The main plate section is not actually flat, but for design purposes that
# isn't overly important.

plate_thickness = 6.

xu = 150.
yu = 80.

xd = 130.
yd = -60.


def place_mounting_holes(obj):
    return place_n_at_x_around(3, 20, obj)


def projection():
    cu = 50.
    cd = -50.

    def arm(points, d):
        return sp.hull()(
            [sp.translate(p)(sp.circle(d=d, segments=32)) for p in points]
        )

    return sp.union()(
        sp.square((100, 100), center=True),
        arm(((-xu, yu), (0, cu)), 20),
        arm(((xu, yu), (0, cu)), 20),
        arm(((-xd, yd), (0, cd)), 20),
        arm(((xd, yd), (0, cd)), 20),
    ) - place_mounting_holes(sp.circle(d=4.5, segments=32))


@bom.part('Steering Wheel')
def volume():
    def handle_bar(points, d):
        return sp.union()(
            [
                sp.hull()(
                    sp.translate(points[i])(sp.sphere(d=d, segments=32)),
                    sp.translate(points[i + 1])(sp.sphere(d=d, segments=32)),
                ) for i in range(len(points) - 1)
            ]
        )

    return sp.union()(
        sp.linear_extrude(plate_thickness, center=True)(projection()),
        handle_bar(((-xd, yd), (-xu, yu), (-xu, yu + 20.)), 20),
        handle_bar(((xd, yd), (xu, yu), (xu, yu + 20.)), 20),
    )


if __name__ == '__main__':
    entrypoint.main(volume())
