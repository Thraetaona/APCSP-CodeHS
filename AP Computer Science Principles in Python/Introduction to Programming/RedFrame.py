"""
 This program has Karel paint a red
 frame around the edge of the world.
"""

""" 
 Paints a red row starting at Karel's starting
 position and ending at the next wall.
"""
def paint_red_row():
    while front_is_clear():
        paint(color["red"])
        move()
    paint(color["red"])

for i in range(4):
    paint_red_row()
    turn_left()