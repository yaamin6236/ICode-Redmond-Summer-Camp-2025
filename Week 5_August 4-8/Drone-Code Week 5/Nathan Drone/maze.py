from easytello import tello


drone = tello.Tello()

drone.takeoff()
drone.up(25)
drone.forward(400)
drone.forward(200)
drone.forward(125)
drone.right(50)
drone.forward(50)
drone.right(50)
drone.back(50)
drone.left(25)
drone.back(25)


drone.land()