""" This is the Scratchpad!
This file is not graded, but you can use it to test your code.

You can write and test your function in the Scratchpad, but make
sure to copy and paste it into the Unit Test file before checking
your answer. Remember to only copy and paste the function you want
to submit, not all of your tests.
"""

# Add your own tests here
# fill in the `citation` function to return the author's name in the correct format
def citation(author_name):
    return str(author_name[2]) + ", " + str(author_name[0]) + " " + str(author_name[1])
    
    
x = citation(("J.", "D.", "Salinger"))
# => "Salinger, J. D."
print(x)
x = citation(("Ursula", "K.", "Le Guin"))
# => "Le Guin, Ursula K."
print(x)
x = citation(("J.", "K.", "Rowling"))
# => "Rowling, J. K."
print(x)