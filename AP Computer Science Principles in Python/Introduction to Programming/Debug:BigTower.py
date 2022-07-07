# This program draws a big tower from Karel's starting spot

# This function has karel face north, no matter what direction
# karel starts facing.
def turn_north():
    while not facing_north():
        turn_left()

# This function builds a tower all the way to the top of the world.
def build_tower():
    while front_is_clear():
        put_ball()
        move()
    put_ball()    

turn_north()
build_tower()