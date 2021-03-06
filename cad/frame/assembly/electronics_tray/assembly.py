import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import bec_module, lighting_control_board, logic_board, placements, relay_board, tray, vesc, vesc_fan
from .dimensions import tray_thickness


def assembly():
    return sp.union()(
        sp.color('red')(tray.volume()),
        spu.up(tray_thickness)(
            sp.color('purple')(placements.vesc_fan(vesc_fan.assembly())),
            # Boards are raised by spacers
            spu.up(3.)(
                sp.color('green')(placements.vesc(vesc.volume())),
                sp.color('blue')(
                    placements.lighting_control_board(
                        lighting_control_board.volume()
                    )
                ),
                sp.color('cyan')(placements.relay_board(relay_board.volume())),
                sp.color('magenta')(placements.bec_module(bec_module.volume())),
                sp.color('orange')(
                    placements.logic_board(logic_board.volume())
                ),
            ),
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
