""" This is the Scratchpad!
This file is not graded, but you can use it to test your code.

You can write and test your function in the Scratchpad, but make
sure to copy and paste it into the Unit Test file before checking
your answer. Remember to only copy and paste the function you want
to submit, not all of your tests.
"""

# Add your own tests here
# this function should return the number of words that contain "owl"!
def owl_count(text):
    
    text_list = text.split()
    
    counter = 0
    
    for i in range(0, len(text_list)):
        if "owl" in text_list[i]:
            counter += 1
    return counter
