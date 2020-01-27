import solid as sp
import solid.utils as spu

from frame.materials import plate
from frame.utils import entrypoint

from .. import common
from ..dimensions import thickness

# TODO
size = (100., 100.)
y_offset = 10.


def projection():
    return spu.back(y_offset)(plate.projection(size)) - common.bearing_holes()


def volume():
    return sp.linear_extrude(thickness, center=True)(projection())


if __name__ == '__main__':
    entrypoint.main(projection())
