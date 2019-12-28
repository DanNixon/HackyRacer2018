import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import lighting_control_board, placements, tray, vesc
from .dimensions import tray_thickness


def assembly():
    return sp.union()(
        sp.color('red')(tray.volume()),
        spu.up(tray_thickness)(
            sp.color('green')(placements.vesc()(vesc.volume())),
            sp.color('blue')(
                placements.lighting_control_board()(
                    lighting_control_board.volume()
                )
            ),
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
