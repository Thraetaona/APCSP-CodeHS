""" This was a hastily written solution not a thought-on one! """

""" As long as there is always a fence in first row """
while front_is_clear():
    move()
turn_left()
    
while front_is_clear():
    if not right_is_clear():
        put_ball()
    """ Could have used else-if here instead. """
    if front_is_clear():
        move()
        
if not right_is_clear():
    put_ball()