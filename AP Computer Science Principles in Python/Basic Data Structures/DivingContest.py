""" This is the Scratchpad!
This file is not graded, but you can use it to test your code.

You can write and test your function in the Scratchpad, but make
sure to copy and paste it into the Unit Test file before checking
your answer. Remember to only copy and paste the function you want
to submit, not all of your tests.
"""

# Add your own tests here
# fill in this function to return the total of the three judges' scores!
def calculate_score(judge_scores):
    return int(judge_scores[0]) + int(judge_scores[1]) + int(judge_scores[2])
    
print(calculate_score((10, 10, 10)))
print(calculate_score((10, 10, 9)))