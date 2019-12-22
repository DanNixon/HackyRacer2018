#!/usr/bin/env python3

import solid as sp
import solid.utils as spu

from frame.assembly import outer
from frame.materials import plate
from frame.utils import entrypoint, place_at_centres

width = 2. * outer
height = 150

magic_1 = 20
magic_2 = 50


def assembly():
    d = (height / 2.) - magic_1

    panel = spu.forward(d)(
        plate.volume(size=(width, height), thickness=8, radius=10, center=True)
    )

    mounting_holes = place_at_centres(
        [width - magic_2, 0], sp.cylinder(d=8, h=50, center=True)
    )

    return panel - mounting_holes


if __name__ == '__main__':
    entrypoint.main(assembly())
