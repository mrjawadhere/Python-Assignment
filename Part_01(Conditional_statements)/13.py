# Perform arithmetic operations.
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == "+":
    print(f"The result is {a + b}.")
elif operator == "-":
    print(f"The result is {a - b}.")
elif operator == "*":
    print(f"The result is {a * b}.")
elif operator == "/" and b != 0:
    print(f"The result is {a / b}.")
else:
    print("Invalid operator or division by zero.")
