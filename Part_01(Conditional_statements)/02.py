# Determine if the user is a minor, adult, or senior citizen based on age.
age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif 18 <= age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
