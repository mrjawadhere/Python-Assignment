# Calculate the sum of the digits of an integer.


number = int(input("Enter an integer: "))
sum_of_digits = 0

while number != 0:
    sum_of_digits += number % 10
    number //= 10

print(f"The sum of the digits is {sum_of_digits}.")

