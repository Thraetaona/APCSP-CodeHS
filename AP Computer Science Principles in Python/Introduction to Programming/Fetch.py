"""
Foreword:
We could finish this assignment just by "hard coding" the steps too,
considering the fact that the only world we have is not even 
dynamic, but then where would the actual "Challenge" in here be?
Well we could also design this program in such a way that it works with any
generic case and world, not just this specific one, but since there already
is a similar task after this and there are not any bonus points for doing so,
we will go with the hard-coding method.
"""


# This function will place karel on top of the existing shelf[*] facing east.
#
# [*]: A shelf is defined as a single horizontal wall in the grid,
# other than the floors and ceilings. (In our case we know where it is)
def relocate_to_shelf():
    move()
    turn_left()
    for _ in range(4):
        move()
    turn_right()
    move()
    
relocate_to_shelf()
take_ball()

turn_around()
move()
move()
turn_left()
for _ in range(4):
    move()

put_ball()
turn_left()