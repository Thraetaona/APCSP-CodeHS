NUM_CIRCLES = 15

# This graphics program should draw a worm. 
# A worm is made up of NUM_CIRCLES circles. 
# Use a for loop to draw the worm, 
# centered vertically in the screen. 
# Also, be sure that the worm is still drawn across 
# the whole canvas, even if the value of NUM_CIRCLES is changed.

center_x = get_width()/2
center_y = get_height()/2

radius = get_width()/NUM_CIRCLES/2
offset = radius/NUM_CIRCLES

parity = 0

for _ in range(NUM_CIRCLES):
    part = Circle(radius)
    part.set_position(0-(offset)+part.get_radius(), center_y)
    
    if (parity%2)==0:
        part.set_color(Color.red)
    else:
        part.set_color(Color.green)
    
    add(part)
    
    offset -= radius*2
    parity += 1