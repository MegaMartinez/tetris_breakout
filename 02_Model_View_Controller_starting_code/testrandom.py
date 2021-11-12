# This is just a test function for random number generators
# Some of the code from this was used in game.py for the function that chooses a random tetromino
# This test made by Matthew Martinez

import random

iold = -5
finalcountA = 0

for k in range(1000):
    i = random.randrange(0, 7, 1)
    if i == iold:
        finalcountA += 1
    else:
        iold = i

iold = ""
finalcountB = 0

for k in range(1000):
    i = random.choice(["I", "J", "L", "O", "T", "S", "Z"])
    if i == iold:
        finalcountB += 1
    else:
        iold = i

iold = ""
finalcountC = 0
i = None

for k in range(1000):
    letterlist = ["I", "J", "L", "O", "T", "S", "Z"]
    if i != None:
        letterlist.remove(i)
    i = random.choice(letterlist)
    if i == iold:
        finalcountC += 1
    else:
        iold = i

print()
print()
print()
print("The same result occurred", finalcountA, "times with randrange()")
print()
print()
print("The same result occurred", finalcountB, "times with choice()")
print()
print()
print("The same result occurred", finalcountC, "times with my new function")
print()
print()
print()
