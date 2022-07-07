def safe_take_ball():
    if balls_present():
        take_ball()

safe_take_ball()
move()
safe_take_ball()