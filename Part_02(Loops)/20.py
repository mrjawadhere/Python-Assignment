# Simulate a countdown timer starting from a given number down to zero.

import time

countdown_start = int(input("Enter the countdown starting number: "))

for i in range(countdown_start, -1, -1):
    print(i)
    time.sleep(1)  # Pauses execution for 1 second
print("Time's up!")
