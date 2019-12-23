import solid as sp
import solid.utils as spu

from frame.utils import entrypoint, place_at_centres
from frame.primitives import drilled_hole

# TODO: check dimensions
diameter = 80
thickness = 15


def holes():
    # TODO: check dimensions
    return sp.union()(
        sp.down(40)(place_at_centres([10, 0], drilled_hole.projection(2))),
        sp.down(30)(drilled_hole.projection(10)),
    )


def projection():
    return sp.circle(d=diameter)


def volume():
    return sp.linear_extrude(thickness)(projection())


if __name__ == '__main__':
    entrypoint.main(projection())
