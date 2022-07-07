# This function draws a circle, given
# the radius, color, and x, y position
# for the center
def draw_circle(radius, color, x, y):
    circ = Circle(radius)
    circ.set_color(color)
    circ.set_position(x, y)
    add(circ)

draw_circle(40, Color.red, 100, 200)
draw_circle(50, Color.green, 50, 100)
draw_circle(70, Color.blue, get_width()/2, get_height()/2)