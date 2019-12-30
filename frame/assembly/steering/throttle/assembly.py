import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import lever, mount
from .dimensions import pot_offset

# angle = 60.
angle = 0.


def assembly():
    return sp.union()(
        sp.color('red')(
            spu.translate(pot_offset)(
                sp.rotate((0, 90, 0))(
                    sp.rotate((0, 0, -110. + angle))(lever.volume())
                )
            )
        ),
        sp.color('green')(mount.volume()),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
