import solid as sp


def test_box_section_projection():
    import frame.materials.box_section as box_section
    thing = box_section.projection()
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_box_section_volume():
    import frame.materials.box_section as box_section
    thing = box_section.volume(100)
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_plate_projection():
    import frame.materials.plate as plate
    thing = plate.projection([100, 50])
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_plate_volume():
    import frame.materials.plate as plate
    thing = plate.volume([100, 50], 3)
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_tube_projection():
    import frame.materials.tube as tube
    thing = tube.projection(25)
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_tube_volume():
    import frame.materials.tube as tube
    thing = tube.volume(25, 100)
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000
