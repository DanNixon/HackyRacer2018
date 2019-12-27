import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import lever, mount
from .dimensions import pot_offset, pot_angle


def assembly():
    return sp.union()(
        sp.color('red')(
            spu.down(pot_offset)(
                sp.rotate((0, 90, pot_angle))(
                    sp.rotate((0, 0, -90))(lever.volume())
                )
            )
        ),
        sp.color('green')(mount.volume()),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
