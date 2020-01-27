import solid as sp

from frame.materials import plate
from frame.utils import entrypoint

from .. import common
from ..dimensions import thickness

# TODO
size = (80., 100.)


def projection():
    return plate.projection(size) - common.bearing_holes()


def volume():
    return sp.linear_extrude(thickness, center=True)(projection())


if __name__ == '__main__':
    entrypoint.main(projection())
