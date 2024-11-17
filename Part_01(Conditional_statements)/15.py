# Check if a number is within a range.
number = int(input("Enter a number: "))
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

if lower <= number <= upper:
    print("The number is within the range.")
else:
    print("The number is outside the range.")
