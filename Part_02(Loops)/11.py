#  Print the reverse of a given number.

number = int(input("Enter a number: "))
reverse = 0

while number != 0:
    reverse = reverse * 10 + number % 10
    number //= 10

print(f"The reverse of the number is {reverse}.")
