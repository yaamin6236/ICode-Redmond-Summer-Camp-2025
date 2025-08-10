from easytello import tello

drone = tello.Tello()

MOVE_COST = 10

ROTATE_COST = 30

def execute_command(cmd):

    global drone, MOVE_COST, ROTATE_COST

    if cmd == "1":
        drone.takeoff()
    elif cmd == "2":
        drone.land()
    elif cmd == "w":
        drone.up(MOVE_COST)
    elif cmd == "a":
        drone.left(MOVE_COST)
    elif cmd == "s":
        drone.down(MOVE_COST)
    elif cmd == "d":
        drone.right(MOVE_COST)
    elif cmd == "q":
        drone.ccw(ROTATE_COST)
    elif cmd == "e":
        drone.cw(ROTATE_COST)


def user_command():

    possible_commands = [
        '1',
        '2',
        'w',
        'a',
        's',
        'd',
        'e',
        'o',
        'p',
    ]
    menu()
    u_input = input("Enter your command: ").lower()
    while not (u_input in possible_commands):
        os.system('clear')
        menu()
        u_input = input("Enter your command: ").lower()
    return u_input


def menu():
    global MOVE_COST, ROTATE_COST
    move = MOVE_COST
    rot = ROTATE_COST
    print("user manual")
    print("1: Takeoff")
    print("2:  Land"({}).format(move))
    print("w: up({})".format(move))
    print("a: left({})".format(move))
    print("s: down({})".format(move))
    print("d: right({})".format(move))
    print("e: cw({})".format(move))
    print("q: ccw({})".format(move))

def main():
    while True:
        command = user_command()
        execute_command(command)

    if_main_=="main"
     main()


