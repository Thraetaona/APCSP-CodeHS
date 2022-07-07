def checked_move():
    if front_is_clear():
        move()

# Clean column logic would also work.
def clean_row():
    while front_is_clear():
        paint(color['black'])
        move()
        paint(color['red'])
        checked_move()
        
    paint(color['red'])

# I know that AND and NOT logical gates are not taught yet but I used it because
# it is cleaner to implement it like this, otherwise we could for example use
# a single-condition while loop (Or even infinite) alongside nested if's.
clean_row() # A "hack" or workaround to make this work on single-row only worlds.
while not ((facing_east() and left_is_blocked()) or (facing_west() and right_is_blocked())):
    # We rotate to left or right depending on the direction we face.
    if facing_east():
        turn_left()
        checked_move()
        turn_left()
    else:
        turn_right()
        checked_move()
        turn_right()
    clean_row()


turn_left()
while front_is_clear():
    move()
    
turn_left()

# We could also define both clean_row() and clean_column() and check when to use
# Each one, but the above method is shorter.
# Even though using clean_row for a one column world or vice versa would be
# very inefficient. (But optimizations and the O(n) notation are another topic.)
# so it would be too soon to employ those methods here.