import itertools

import solid as sp


def place_at_centres(centres, obj):
    _x = [-centres[0] / 2, centres[0] / 2]
    _y = [-centres[1] / 2, centres[1] / 2]

    return [sp.translate([x, y])(obj) for x, y in itertools.product(_x, _y)]
