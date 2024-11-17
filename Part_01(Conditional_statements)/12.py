# Determine temperature category.
temperature = float(input("Enter temperature in Celsius: "))

if temperature <= 0:
    print("It's freezing.")
elif 1 <= temperature <= 25:
    print("It's moderate.")
else:
    print("It's hot.")
