# Continue to ask for a number until the correct number is guessed.

correct_number = 7  # You can change this value
guess = -1

while guess != correct_number:
    guess = int(input("Guess the number: "))
    if guess != correct_number:
        print("Wrong guess! Try again.")
print("You guessed it!")
