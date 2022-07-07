# This function will stack exactly 3 tennis balls on top of eachother starting
# from the position of the place Karel is when this is called.
#
# It is required as a pre-condition that there is enough space (3) above Karel
# and that he is facing east.
# 
# Upon completing said tower, Karel will end up at the same position and
# direction as it was before.
def build_tower():
    turn_left()
    for _ in range(0, 2):
        put_ball()
        move()
    put_ball()
    
    turn_around()
    for _ in range(0, 2):
        move()
        
    turn_left()
    

# Start placing balls every odd column starting from (1, 1), Facing east.  
build_tower()

while front_is_clear():
    move()
    if front_is_clear():
        move()
        build_tower()