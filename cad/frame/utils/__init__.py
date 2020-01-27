import itertools

import solid as sp
import solid.utils as spu


def split_centers(d):
    return [-d / 2., d / 2.]


def place_at_centres(centers, obj):
    cx = split_centers(centers[0])
    cy = split_centers(centers[1])

    return [sp.translate([x, y])(obj) for x, y in itertools.product(cx, cy)]


def place_n_at_x_around(n, x, obj):
    return [
        sp.rotate([0, 0, a * 360. / n])(spu.forward(x)(obj)) for a in range(n)
    ]
