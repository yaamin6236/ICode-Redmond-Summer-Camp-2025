def add(num1, num2):
    print(num1 + num2)

def subtract(num1, num2):
    print(num1 - num2)

def multiply(num1, num2):
    print(num1 * num2)

def divide(num1, num2):
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        print(num1 / num2)

# Get user inputs and convert to floats
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter +, -, *, /: ")

    if operation == "+":
        add(num1, num2)
    elif operation == "-":
        subtract(num1, num2)
    elif operation == "*":
        multiply(num1, num2)
    elif operation == "/":
        divide(num1, num2)
    else:
        print("Invalid operation.")
except ValueError:
    print("Please enter valid numbers.")
