"""
This program has Karel invert colors
"""

""" For red and blue only! """
def invert_color():
    if color_is(color["red"]):
        paint(color["blue"])
    else:
        paint(color["red"])
        
while front_is_clear():
    invert_color()
    move()

invert_color()