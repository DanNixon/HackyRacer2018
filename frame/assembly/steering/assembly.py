import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import mount, wheel


def assembly():
    return sp.union()(
        sp.color('red')(wheel.volume()),
        sp.color('green')(
            spu.down(wheel.plate_thickness / 2.)(
                sp.rotate((0, 180, 0))(mount.volume())
            )
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
