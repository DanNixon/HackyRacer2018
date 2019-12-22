import solid as sp


def test_brake_disc_projection():
    import frame.parts.brake_disc as brake_disc
    thing = brake_disc.projection()
    print(sp.scad_render(thing))


def test_brake_disc_volume():
    import frame.parts.brake_disc as brake_disc
    thing = brake_disc.volume()
    print(sp.scad_render(thing))


def test_brake_disc_mount_volume():
    import frame.parts.brake_disc_mount as brake_disc_mount
    thing = brake_disc_mount.volume()
    print(sp.scad_render(thing))


def test_drive_sprocket_projection():
    import frame.parts.drive_sprocket as drive_sprocket
    thing = drive_sprocket.projection()
    print(sp.scad_render(thing))


def test_drive_sprocket_volume():
    import frame.parts.drive_sprocket as drive_sprocket
    thing = drive_sprocket.volume()
    print(sp.scad_render(thing))


def test_drive_sprocket_mount_volume():
    import frame.parts.drive_sprocket_mount as drive_sprocket_mount
    thing = drive_sprocket_mount.volume()
    print(sp.scad_render(thing))


def test_lighting_control_board_volume():
    import frame.parts.lighting_control_board as lighting_control_board
    thing = lighting_control_board.volume()
    print(sp.scad_render(thing))


def test_motor_volume():
    import frame.parts.motor as motor
    thing = motor.volume()
    print(sp.scad_render(thing))


def test_rear_axle_bearing_volume():
    import frame.parts.rear_axle_bearing as rear_axle_bearing
    thing = rear_axle_bearing.volume()
    print(sp.scad_render(thing))


def test_motor_mountable_face():
    import frame.parts.motor as motor
    thing = motor.mountable_face()
    print(sp.scad_render(thing))


def test_vesc_volume():
    import frame.parts.vesc as vesc
    thing = vesc.volume()
    print(sp.scad_render(thing))


def test_wheel_volume():
    import frame.parts.wheel as wheel
    thing = wheel.volume()
    print(sp.scad_render(thing))
