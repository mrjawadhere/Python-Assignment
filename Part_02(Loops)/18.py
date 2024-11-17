# Print numbers in reverse order within a given range.

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for i in range(start, end - 1, -1):
    print(i)
