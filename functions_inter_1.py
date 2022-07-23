"""If no arguments are provided, the function should return a random integer between 0 and 100.
If only a max number is provided, the function should return a random integer between 0 and the max number.
If only a min number is provided, the function should return a random integer between the min number and 100
If both a min and max number are provided, the function should return a random integer between those 2 values.
(Create this function without using random.randInt() -- we are trying to build that method ourselves for this assignment!)"""

import random

def randInt(min= 0 , max= 100):
    possible_range = max - min
    if max < 0:
        return f"Your max must be greater than zero!"

    elif min > max:
        return f"Your min can't be greater than your max!"

    return round(random.random()* possible_range + min)

print(randInt())
print(randInt(min=10))
print(randInt(max = 20))
print(randInt(min = 5, max = 15))
print(randInt(min=30, max=20))
print(randInt(max=-3))