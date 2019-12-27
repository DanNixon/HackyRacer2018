import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import instrument_panel, mount, wheel


def assembly():
    return sp.union()(
        spu.up(mount.length)(
            spu.up(wheel.plate_thickness / 2.)(
                sp.color('red')(wheel.volume()),
                spu.up(wheel.plate_thickness / 2.)(
                    sp.color('green')(
                        spu.left(50)(instrument_panel.left.volume(), ),
                        spu.right(50)(instrument_panel.right.volume(), ),
                    ),
                ),
            ),
            sp.color('blue')(sp.rotate((0, 180, 0))(mount.volume())),
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
