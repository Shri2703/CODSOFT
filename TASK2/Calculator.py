def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "cannot divide by zero"

def Calculator():
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}
    print("Simple Calculator")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue  # Go back to the beginning of the loop if invalid input

        operation = input("Choose operation (+, -, *, /) or 'stop' to exit: ")

        if operation.lower() == 'stop':
            print("Calculator stopped.")
            break  # Exit the loop and end the program

        if operation in operations:
            result = operations[operation](num1, num2)
            print(f"Result: {result}")
        else:
            print("Invalid operation. Please choose a valid operation (+, -, *, /).")


# Run the calculator
Calculator()
