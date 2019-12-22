#!/usr/bin/env python3

import solid as sp

from frame.utils import bom, place_n_at_x_around

# XX tooth
outer_diameter = 140

# 74 tooth
# outer_diameter = 190;

thickness = 3


def place_mounting_holes(obj):
    return place_n_at_x_around(3, 20, obj)


def projection():
    outer = sp.circle(d=outer_diameter)
    inner = sp.circle(d=26)
    mounting_holes = place_mounting_holes(sp.circle(d=6))
    return outer - inner - mounting_holes


@bom.part('Drive Sprocket')
def volume():
    return sp.linear_extrude(thickness)(projection())


if __name__ == '__main__':
    print(sp.scad_render(volume()))
