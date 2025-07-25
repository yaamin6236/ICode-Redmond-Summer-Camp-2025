from djitellopy import Tello
def fly():
    pass
def main():
    tello = Tello()
    for i in range(3):
        tello.connect()
        tello.takeoff()
        tello.flip("f")
        tello.flip("b")
        tello.flip("l")
        tello.flip("r")
        tello.land()
        tello.takeoff()
        tello.flip("f")
        tello.flip("b")
        tello.flip("l")
        tello.flip("r")
        tello.land()