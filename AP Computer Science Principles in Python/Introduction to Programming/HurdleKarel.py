def run_to_finish():
    move()
    move()
    move()
    move()

def run_to_hurdle():
    move()
    move()
    move()

def jump_hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

run_to_hurdle()
jump_hurdle()
run_to_hurdle()
jump_hurdle()
run_to_finish()