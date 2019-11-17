import solid as sp


def test_box_section_projection():
    import frame.materials.box_section as box_section
    print(sp.scad_render(box_section.projection()))


def test_box_section_volume():
    import frame.materials.box_section as box_section
    print(sp.scad_render(box_section.volume(100)))


def test_plate_projection():
    import frame.materials.plate as plate
    print(sp.scad_render(plate.projection([100, 50])))


def test_plate_volume():
    import frame.materials.plate as plate
    print(sp.scad_render(plate.volume([100, 50], 3)))


def test_tube_projection():
    import frame.materials.tube as tube
    print(sp.scad_render(tube.projection(25)))


def test_tube_volume():
    import frame.materials.tube as tube
    print(sp.scad_render(tube.volume(25, 100)))
