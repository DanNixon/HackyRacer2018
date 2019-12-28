import solid as sp

from frame.assembly.dimensions import inner
from frame.utils import bom, entrypoint, place_at_centres

from . import can_bus_board, lighting_control_board, placements, relay_board, vesc
from .dimensions import tray_dimensions, tray_thickness

mounting_hole_centres = (inner * 2., tray_dimensions[1] - 20.)
mounting_hole_diameter = 3.5


def projection():
    panel = sp.square(tray_dimensions, center=True)

    frame_mounting_holes = place_at_centres(
        mounting_hole_centres, sp.circle(d=mounting_hole_diameter, segments=32)
    )

    return panel - frame_mounting_holes - placements.vesc()(
        vesc.holes()
    ) - placements.lighting_control_board()(
        lighting_control_board.holes()
    ) - placements.can_bus_board()(
        can_bus_board.holes()
    ) - placements.relay_board()(relay_board.holes())


@bom.part('Electronics Tray')
def volume():
    return sp.linear_extrude(tray_thickness)(projection())


if __name__ == '__main__':
    entrypoint.main(projection())
