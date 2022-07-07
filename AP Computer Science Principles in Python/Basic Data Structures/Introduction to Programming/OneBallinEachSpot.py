def checked_ball_placement():
    if no_balls_present():
        put_ball()

checked_ball_placement # Initializer
for _ in range(0, 3):
    move()
    checked_ball_placement()