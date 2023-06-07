#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNumber = abs(number) % 10
lastNumber = -lastNumber if number < 0 else lastNumber
print(f"Last digit of {number:d} is {lastNumber}", end=" ")
if lastNumber > 5:
    print(f"and is greater than 5")
elif number < 0 and lastNumber != 0 or lastNumber <= 5 and lastNumber != 0:
    print(f"and is less than 6 and not 0")
else:
    print(f"and is 0")
