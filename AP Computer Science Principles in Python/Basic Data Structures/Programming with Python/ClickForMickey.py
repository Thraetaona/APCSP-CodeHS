import random
# Constants for body
HEAD_RADIUS = 30
EAR_RADIUS = 20
EAR_OFFSET = HEAD_RADIUS

'''
This is a tuple.  It assigns a list of values to a single
variable. You can see how it is used here, but you do not
need  to know all the details. We will learn more about 
tuples and lists in a later module.
'''
COLORS = (Color.red, Color.orange, Color.yellow, 
          Color.green, Color.blue, Color.black)

# Helper function to draw a circle
def draw_circle(x, y, radius, color):
    circle = Circle(radius)
    circle.set_position(x, y)
    circle.set_color(color)
    add(circle)

def make_mickey(x, y):
    
    # random.choice returns a random value from the COLORS
    # tuple we defined above. We will learn more about random
    # soon.
    color = random.choice(COLORS) 
    
    #Draw the head
    draw_circle(x, y, HEAD_RADIUS, color)
    
    #Draw the left ear - up  and to the left of the head
    draw_circle(x - EAR_OFFSET, y - EAR_OFFSET, EAR_RADIUS, color)
    
    #Draw the right ear - up and to the right of the head
    draw_circle(x + EAR_OFFSET, y - EAR_OFFSET, EAR_RADIUS, color)

add_mouse_click_handler(make_mickey)