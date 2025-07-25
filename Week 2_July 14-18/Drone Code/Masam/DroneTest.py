from djitellopy import Tello 

def fly():
    pass

def main():
    tello = Tello()

    tello.connect()

    tello.takeoff()
    
    tello.move_up(100)

    tello.rotate_clockwise(360)
    tello.move_left(50)
    tello.rotate_clockwise(360)
    tello.move_right(50)
    tello.rotate_clockwise(360)
    tello.land()


if __name__ == "main":
    main()