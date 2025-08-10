from easytello import tello
drone = tello.Tello()


for i in range (2):
    drone.takeoff()
    drone.up(15)
    drone.forward(100)
    drone.land()





























