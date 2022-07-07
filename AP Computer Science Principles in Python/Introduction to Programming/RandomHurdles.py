def jump_hurdles():
    if not (front_is_clear()):
        # Actual Jumping
        # This does not check for ceilings or tall hurdles.
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        
for _ in range(0, 13):
    if (front_is_clear()):
        move()
    else:
        jump_hurdles()