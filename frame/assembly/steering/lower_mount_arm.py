import solid as sp
import solid.utils as spu

from frame.materials import flat_bar
from frame.utils import entrypoint

from . import lower_mount

length = 60.
thickness = flat_bar.default_size[1]

magic_1 = (lower_mount.face_diameter / 2.) - 5.


def volume():
    # TODO: mounting holes
    return sp.translate((0., magic_1, thickness / 2.))(
        sp.rotate((90, 0, 0))(flat_bar.volume(length=length + magic_1))
    )


if __name__ == '__main__':
    entrypoint.main(volume())
