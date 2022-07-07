"""
  This program has karel jump over two
  hurdles and then move all of the way
  to the edge of the world.
 """

"""
 Precondition: Karel has just jumped the
 last hurdle, and is facing east.
 Postcondition: Karel is all of the way
 at the end of the world.
"""
def run_to_finish():
    move()
    move()
    move()
    move()

"""
 Precondition: Karel is facing east, three
 spots away from a hurdle.
 Postcondition: Karel is standing right in  front of a hurdle.
"""
def run_to_hurdle():
    move()
    move()
    move()

""" 
  This function has karel jump over a 
  hurdle that is one row high.
 Precondition: Karel is standing in front 
 of a hurdle, facing east.
 Postcondition: Karel has just jumped over 
 a hurdle, and is facing east.
"""
def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Karel jumps two hurdles in this
# program.
run_to_hurdle()
jump_hurdle()
run_to_hurdle()
jump_hurdle()
run_to_finish()