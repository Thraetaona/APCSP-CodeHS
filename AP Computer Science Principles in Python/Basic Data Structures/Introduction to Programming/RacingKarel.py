# This program will have Karel run around the racetrack
# 8 times.

# This function will run around a generic racetrack (As defined by the question)
# While "decorating" its corners by using tennis balls.
def decorate_lap():
    for _ in range(4):
        while front_is_clear():
            move()
            
        put_ball()
        turn_left()
        
        
# Run and decorate the lap 8 times as requested.
for _ in range(8):
    decorate_lap()