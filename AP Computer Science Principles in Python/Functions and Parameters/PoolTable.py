POOL_BALL_RADIUS = 40
FONT_TYPE = "30pt Arial"


# Write a function called draw_pool_ball that draws a pool ball.
def draw_pool_ball(color, num, x, y):
    # Add your code here
    circ = Circle(POOL_BALL_RADIUS)
    circ.set_color(color)
    circ.set_position(x, y)
    add(circ)
    
    
    txt = Text(num)
    txt.set_color(Color.white)
    txt.set_position(x-txt.width, y+txt.height/2)
    txt.set_font(FONT_TYPE)
    add(txt)

draw_pool_ball(Color.orange, 5, 100, 100)
draw_pool_ball(Color.red, 3, 150, 350)
draw_pool_ball(Color.blue, 2, 250, 140)
draw_pool_ball(Color.green, 6, 50, 200)