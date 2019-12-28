import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import can_bus_board, lighting_control_board, placements, relay_board, tray, vesc
from .dimensions import tray_thickness


def assembly():
    return sp.union()(
        sp.color('red')(tray.volume()),
        spu.up(tray_thickness)(
            sp.color('green')(placements.vesc()(vesc.volume())),
            # Boards are raised by spacers
            spu.up(3.)(
                sp.color('blue')(
                    placements.lighting_control_board()(
                        lighting_control_board.volume()
                    )
                ),
                sp.color('green')(
                    placements.can_bus_board()(can_bus_board.volume())
                ),
                sp.color('cyan')(
                    placements.relay_board()(relay_board.volume())
                ),
            ),
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
