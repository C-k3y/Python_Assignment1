# Asks the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Asks the user to choose an operation
operation = input("Choose an operation (+, -, *, /): ")

# Performs the operation
if operation == "+":
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")
else if operation == "-":
    difference = num1 - num2
    print(f"{num1} - {num2} = {difference}")
else if operation == "*":
    multiplication = num1 * num2
    print(f"{num1} * {num2} = {multiplication}")
else if operation == "/":
    if num2 != 0:
        division = num1 / num2
        print(f"{num1} / {num2} = {division}")
    else:
        print("Error: You cannot divide a number with zero!")
else:
    print("Invalid operation. Please choose +, -, *, or /.")
