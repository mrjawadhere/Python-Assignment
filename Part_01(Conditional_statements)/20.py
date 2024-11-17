#Check if a number is prime.

number = int(input("Enter a number: "))

if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("The number is not prime.")
            break
    else:
        print("The number is prime.")
else:
    print("The number is not prime.")
