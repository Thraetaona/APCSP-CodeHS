import random

set_size(480, 400)

# This graphics program should draw a square. 
# The fill color should be randomly choosen from
# the COLORS list

SIDE_LENGTH = 100
COLORS = [Color.red, Color.orange, Color.yellow, Color.green, Color.blue, 
        Color.purple, Color.black, Color.gray]
        


random_color = random.choice(COLORS) 

rect = Rectangle(SIDE_LENGTH, SIDE_LENGTH)
rect.set_position(
    get_width()/2 - SIDE_LENGTH/2,
    get_height()/2 - SIDE_LENGTH/2
)


rect.set_color(random_color)
add(rect)