# Check if three sides form a valid triangle.
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if a + b > c and a + c > b and b + c > a:
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")
