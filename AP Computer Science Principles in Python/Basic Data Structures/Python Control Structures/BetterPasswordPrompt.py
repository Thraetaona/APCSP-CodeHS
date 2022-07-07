SECRET = "abc123"
# Enter your code here

    


while (True):

    prompt = str(input("Enter password: "))


    if prompt == SECRET:
        break
    
    print("Sorry, that did not match. Please try again.")

print("You got it!")