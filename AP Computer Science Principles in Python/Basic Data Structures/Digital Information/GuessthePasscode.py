"""
 Write a program that guesses every possible 4 digit passcode
 combinations until the correct passcode is guessed.

 The passcode is randomly generated and stored in the variable
 secretPasscode.

 Print out how many guesses it took to guess the correct passcode.
"""
MAX_AMOUNT = 10000
tries = int(0)

import random

# Checks whether the given guess passcode is the correct passcode
def is_correct(guess_code, correct_code):
    global tries
    tries += 1
    return guess_code == correct_code

# Generates a random 4 digit passcode and returns it as a String
def generate_random_passcode():
    random_passcode = ""
    
    for i in range(4):
        random_digit = random.randint(0, 9)
        random_passcode += str(random_digit)
    return int(random_passcode)

secret_passcode = generate_random_passcode()
# Write your code here
for passcode in range(0, MAX_AMOUNT):
    if is_correct(passcode, secret_passcode):
        print("Passcode found!")
        break

            
    

    
print("The randomly generated passcode was: ", str(secret_passcode))
print("And it took ", str(tries), " tries to guess the correct passcode.")