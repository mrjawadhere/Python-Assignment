# Print a pyramid pattern of * using nested loops.

rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
