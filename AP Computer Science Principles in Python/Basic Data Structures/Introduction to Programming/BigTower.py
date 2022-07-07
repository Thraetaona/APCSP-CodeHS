# This program draws a big tower from Karel's starting spot

while not facing_north():
    turn_left()

if not balls_present():
    put_ball()
    
while front_is_clear():
    if not (balls_present()):
        put_ball()
        
    move()
    
if not (balls_present()):
    put_ball()