#!/usr/bin/env python3

import solid as sp

from frame.utils import bom, place_n_at_x_around

thickness = 2


def place_mounting_holes(obj):
    return place_n_at_x_around(6, 24, obj)


def projection():
    outer = sp.circle(d=140)
    inner = sp.circle(d=38)
    mounting_holes = place_mounting_holes(sp.circle(d=6))
    return outer - inner - mounting_holes


@bom.part('Brake Disc')
def volume():
    return sp.linear_extrude(thickness)(projection())


if __name__ == '__main__':
    print(sp.scad_render(volume()))
