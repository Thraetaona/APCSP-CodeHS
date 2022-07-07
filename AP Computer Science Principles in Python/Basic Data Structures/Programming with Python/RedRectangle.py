# Create a red rectangle at 40, 40
# Make the width  and height 1/3 of the canvas

width = get_width() / 3
height = get_height() / 3

red_rect = Rectangle(width, height)
red_rect.set_color(Color.red)
red_rect.set_position(40, 40)
add(red_rect)