import random
# Enter your code here


MAX = 100
MIN = 0

secret_num = random.randint(MIN, MAX)
guessed_val = int(input("Guess my number that is between " + str(MIN) + " and " + str(MAX) + "."))

while guessed_val != secret_num:
    if (guessed_val >= secret_num):
        guessed_val = int(input("Too high, try again!"))
    elif (guessed_val <= secret_num):
        guessed_val = int(input("Too low, try again!"))
        
print("You found it!")