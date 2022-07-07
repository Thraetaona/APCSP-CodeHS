import random

# Constants for body
RECT_WIDTH = 30
RECT_HEIGHT = 50

COLORS = (
    Color.red, Color.green, Color.blue, 
    Color.orange, Color.yellow, Color.black
)

def draw_randomly_colored_rectangle(x, y):
    random_color = random.choice(COLORS) 
    
    rect = Rectangle(RECT_HEIGHT, RECT_WIDTH)
    rect.set_position(
        x - RECT_WIDTH/2,
        y - RECT_HEIGHT/2
    )
    
    
    rect.set_color(random_color)
    add(rect)


add_mouse_click_handler(draw_randomly_colored_rectangle)