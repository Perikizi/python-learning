"""A simple calculator that performs basic arithmetic operations."""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operator: ")

if operation == '+':
    result = num1 + num2
    print("Result: ", result)
elif operation == '-':
    result = num1 - num2
    print("Result: ", result)
elif operation == '*':
    result = num1 * num2
    print("Result: ", result)
elif operation == '/':
    result = num1 / num2
    print("Result: ", result)
else:
    print("Invalid operator")