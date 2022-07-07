import random


STATES = (bool(True), bool(False))

# Enter your code here

status = bool(random.choice(STATES))

if (status):
    print("Heads")
else:
    print("Tails")