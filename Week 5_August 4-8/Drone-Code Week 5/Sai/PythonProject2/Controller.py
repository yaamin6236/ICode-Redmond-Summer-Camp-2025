from easytello import tello

Drone = tello.Tello()

Drone.takeoff()

Drone.forward(500)

Drone.forward(200)

Drone.flip("f")

Drone.flip("l")

Drone.flip("r")

Drone.flip("b")

Drone.up(50)

Drone.down(50)

Drone.cw(100)

Drone.ccw(500)



for i in range(30):
    Drone.cw(65)

    Drone.left(60)



Drone.land()