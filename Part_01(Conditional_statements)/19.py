# Check if a string is uppercase, lowercase, or mixed.
text = input("Enter a string: ")

if text.isupper():
    print("The string is uppercase.")
elif text.islower():
    print("The string is lowercase.")
else:
    print("The string is mixed case.")
