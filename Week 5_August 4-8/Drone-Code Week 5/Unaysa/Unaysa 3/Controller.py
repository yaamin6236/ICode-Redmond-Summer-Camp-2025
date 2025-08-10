import os

from easytello import tello

Drone=tello.Tello()

MOVE_CONST= 18
ROTATE_CONST= 30


def execute_command(cmd):
    global Drone, MOVE_CONST, ROTATE_CONST

    if cmd == "1":
        Drone.takeoff()
    elif cmd == "2":
        Drone.land()
    elif cmd == "w":
        Drone.forward(MOVE_CONST)
    elif cmd == "s":
        Drone.back(MOVE_CONST)
    elif cmd == "a":
        Drone.left(MOVE_CONST)
    elif cmd == "d":
        Drone.right(MOVE_CONST)
    elif cmd == "e":
        Drone.cw(ROTATE_CONST)
    elif cmd == "q":
        Drone.ccw(ROTATE_CONST)

def user_command():
     possible_command={
         '1',
         '2',
         'w',
         's',
         'a',
         'd',
         'e',
         'q',
         'o',
         'p',

     }
     menu()
     u_input=input("Please enter your command: ").lower()
     while not (u_input in possible_command):
         os.system("clear")
         menu()
         u_input=input("Please enter your command: ").lower()
     return u_input

def menu():

    global MOVE_CONST, ROTATE_CONST
    move=MOVE_CONST
    rot=ROTATE_CONST
    print("User manual:")
    print("1: takeoff()")
    print("2: land({})".format(move))
    print("W: up({})".format(move))
    print("S: down({})".format(move))
    print("A: left({})".format(move))
    print("D: right({})".format(move))
    print("E: cw({})".format(rot))
    print("Q: ccw({})".format(rot))


def main():
    while True:
        command=user_command()
        execute_command(command)


if __name__ == '__main__':
    main()

