num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))
operation = input("Which operation would you like to apply?")

def add(a, b):
    print(a + b)

def multiply(a, b):
    print(a * b)

def divide(a, b):
    print(a/b)

def subtract(a, b):
    print(a-b)

if operation in ["*", "multiply", "x"]:
    multiply(num1, num2)
elif operation in ["+", "add"]:
    add(num1, num2)

elif operation in ["/", "divide"]: 
    print(num1/num2)
elif operation in ["-", "subtract"]:
    print(num1-num2)
else: 
    print("Error, please try again with a valid operation")

