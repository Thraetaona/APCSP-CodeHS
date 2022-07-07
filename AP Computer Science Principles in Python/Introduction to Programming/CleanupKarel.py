while front_is_clear():
    if balls_present():
        take_ball()
    move()

if balls_present():
    take_ball()