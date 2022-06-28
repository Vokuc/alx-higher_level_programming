#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
if 6 > int(last_digit) > 0:
    print(f"Last digit of {number} is {last_digit} and is less than 6 not 0")
elif int(last_digit) > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif int(last_digit) == 0:
    print(f"Last digit of {number} and is 0")
print(number)
