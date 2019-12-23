import solid as sp
import solid.utils as spu

from frame.assembly.dimensions import axle_diameter
from frame.utils import entrypoint

from . import disc
from . import mount


def assembly():
    return sp.union()(
        sp.color('red')(mount.volume()),
        sp.color('green')(spu.down(disc.thickness)(disc.volume())),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
