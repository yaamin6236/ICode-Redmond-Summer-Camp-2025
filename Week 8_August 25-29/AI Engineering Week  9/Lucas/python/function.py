def printhello():
    print("hello")

    printhello()

    print("not intended")

   def printgoodbye():
    print("goodbye")

    printgoodbye()

    print("not intended")

def printhello(name):
    print(f"Hello, {name}!")

def printgoodbye(name):
    print(f"Goodbye, {name}!")

def printgetname():
    name = input("What is your name? ")
    return name

# Main script logic
user_name = printgetname()
printhello(user_name)
printgoodbye(user_name)

printhello()
printgoodbye()
getname()
getname()
printsomething("lolololololololololololol")