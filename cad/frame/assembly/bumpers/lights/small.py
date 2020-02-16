import solid as sp

from frame.utils import entrypoint, place_at_centres
from frame.primitives import drilled_hole

# TODO: check dimensions
diameter = 50
thickness = 6


def holes():
    # TODO: check dimensions
    return place_at_centres([20, 0], drilled_hole.projection(3))


def projection():
    return sp.circle(d=diameter)


def volume():
    return sp.linear_extrude(thickness)(projection())


if __name__ == '__main__':
    entrypoint.main(volume())
