# Moves Karel one block behind facing the same direction as before.
# There should exist a block behind Karel for this to work.
def step_back():
    turn_around()
    move()
    turn_around()

# This will fetch a single ball on Karel's current spot to the front of karel
# There should be an empty block infront of Karel and there can not be no balls.
# It is up to the caller to move Karel back to it's starting position.
#
# Verbose function names are useful to explain what they do at a glance.   
def fetch_ball():
    take_ball()
    move()
    
    put_ball()
    
# This does the same as fetch_ball() except that it adds an extra ball
# to the new location as well.
def fetch_ball_and_double():
    fetch_ball()
    
    put_ball()



""" Main Function """

# Move Karel to the pile of tennis balls on (2, 1).
move()


# No variables... unfortunate, but restrictions flourish creativity.
# 
# So in here we will; for each ball that exists on the spot; take one, move
# one step forward, put down 2 balls, move one step backwards and repeat
# until no more balls exist.
# In this way we can count the number of balls and store them (doubled) in a
# block of our grid (This is still some sort of variable!)
while balls_present():
    fetch_ball_and_double()
    step_back()
    
# Move to the storage area and face the previous position of the starting balls.
move()
turn_around()

# Now that we have the doubled count of our starting balls, we fetch them
# back to their previous position normally.
while balls_present():
    fetch_ball()
    step_back()


# Move Karel back to his starting position (1, 1), facing east.
move()
move()
turn_around()