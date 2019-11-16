import itertools

import solid as sp
import solid.utils as spu


def place_at_centres(centres, obj):
    _x = [-centres[0] / 2, centres[0] / 2]
    _y = [-centres[1] / 2, centres[1] / 2]

    return [sp.translate([x, y])(obj) for x, y in itertools.product(_x, _y)]


def place_n_at_x_around(n, x, obj):
    return [
        sp.rotate([0, 0, a * 360. / n])(spu.forward(x)(obj)) for a in range(n)
    ]
