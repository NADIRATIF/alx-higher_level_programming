#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNumber = abs(number) % 10
print(f"Last digit of {number:d} is {lastNumber}", end=" ")
if lastNumber > 5:
    print(f"and is greater than 5")
elif lastNumber < 6:
    if lastNumber != 0:
        print(f"and is less than 6 and not 0")
else:
    print(f"and os 0")
