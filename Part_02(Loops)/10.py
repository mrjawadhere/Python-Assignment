# Count the number of digits in an integer using a loop.

number = int(input("Enter an integer: "))
count = 0

while number != 0:
    count += 1
    number //= 10

print(f"The number of digits is {count}.")

