import sys

import solid as sp

from frame.utils import bom


def main(thing):
    import sys
    if sys.argv[1] == 'scad_render':
        print(sp.scad_render(thing))
    elif sys.argv[1] == 'bom':
        bom.pretty_print()
