from easytello import tello


mydrone = tello.Tello()

mydrone.takeoff()

mydrone.up(100)

print(mydrone.get_height)

for i in range(3)
    my_forward(35)
    while int(mydrone.get_height()) > 100:
        print(mydrone.get_height())
        mydrone.down(50)

        mydrone.land()














