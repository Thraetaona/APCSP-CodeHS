def turn_right():
    turn_left()
    turn_left()
    turn_left()

def build_tower():
    turn_left()
    move()
    put_ball()
    turn_left()
    turn_left()
    move()
    put_ball()
    turn_left()
    turn_left()
    move()
    move()
    put_ball()
    move()
    
# This way will work as well! Uncomment this code segment and comment the 
# code segment above. 
# When things are abstracted, the details of the abstraction are no longer
# important!

# def build_tower():
#     put_ball()
#     turn_left()
#     move()
#     put_ball()
#     move()
#     put_ball()
#     move()


move()
build_tower()
turn_right()