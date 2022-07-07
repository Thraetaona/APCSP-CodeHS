# Draw a circle at x, y
def draw_circle(x, y):
    circle = Circle(20)
    circle.set_position(x, y)
    add(circle)

# link to the mouse click event
add_mouse_click_handler(draw_circle)