from djitellopy import Tello
def fly():
    pass
def main():
    tello = Tello()
    tello.connect()
    tello.takeoff()
    tello.move_up(75)
    tello.move_down(30)
    tello.move_up(10)
    tello.flip("f")
    tello.flip("b")
    tello.rotate_clockwise(360)
    tello.rotate_counter_clockwise(360)
    tello.flip("l")
    tello.flip("r")
    tello.move_forward
    tello.move_backward
    tello.flip("b")
    tello.land()