import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import arduino_uno, bec_module, can_bus_board, lighting_control_board, placements, relay_board, tray, vesc
from .dimensions import tray_thickness

# TODO: Additional things? VESC fan shroud? PDU board?


def assembly():
    return sp.union()(
        sp.color('red')(tray.volume()),
        spu.up(tray_thickness)(
            sp.color('green')(placements.vesc(vesc.volume())),
            # Boards are raised by spacers
            spu.up(3.)(
                sp.color('blue')(
                    placements.lighting_control_board(
                        lighting_control_board.volume()
                    )
                ),
                sp.color('cyan')(
                    placements.can_bus_board(can_bus_board.volume())
                ),
                sp.color('magenta')(
                    placements.relay_board(relay_board.volume())
                ),
                sp.color('orange')(placements.arduino(arduino_uno.volume())),
                sp.color('lime')(placements.bec_module(bec_module.volume())),
            ),
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
