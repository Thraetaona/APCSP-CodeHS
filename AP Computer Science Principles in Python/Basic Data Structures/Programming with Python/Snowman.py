# Constants representing the radius of the top, middle,
# and bottom snowball.
BOTTOM_RADIUS = 100
MID_RADIUS = 60
TOP_RADIUS = 30

SNOWMAN_COLOR = Color.gray
SNOWMAN_X_POS = get_width()/2

EYE_COLOR = Color.black
EYE_RADIUS = 5

HAT_COLOR = Color.red
HAT_BASE_COLOR = Color.blue
HAT_HEIGHT = 50
HAT_WIDTH = (2*TOP_RADIUS) + EYE_RADIUS

def create_ball(
    radius: int,
    x_pos: int, y_pos: int,
    color: int
):
    ball = Circle(radius)
    ball.set_position(x_pos, y_pos)
    ball.set_color(color)
    
    # Register it
    add(ball)

def create_snowman():
    offset = get_height()
    
    offset -= BOTTOM_RADIUS + 0
    # Bottom Circle
    create_ball(
        BOTTOM_RADIUS,
        SNOWMAN_X_POS, offset,
        SNOWMAN_COLOR
    )

    offset -= BOTTOM_RADIUS + MID_RADIUS
    # Middle Circle
    create_ball(
        MID_RADIUS,
        SNOWMAN_X_POS, offset,
        SNOWMAN_COLOR
    )

    offset -= MID_RADIUS + TOP_RADIUS
    # Top Circle
    create_ball(
        TOP_RADIUS,
        SNOWMAN_X_POS, offset,
        SNOWMAN_COLOR
    )
    
    # Two eyes
    create_ball(
        EYE_RADIUS,
        SNOWMAN_X_POS + (TOP_RADIUS/2), offset,
        EYE_COLOR
    )
    create_ball(
        EYE_RADIUS,
        SNOWMAN_X_POS - (TOP_RADIUS/2), offset,
        EYE_COLOR
    )
    
    
    offset -= 3*TOP_RADIUS
    # Black Hat
    hat = Rectangle(HAT_HEIGHT, HAT_WIDTH)
    hat.set_position(SNOWMAN_X_POS - HAT_HEIGHT/2, offset)
    hat.set_color(HAT_COLOR)
    add(hat)

    hat_base = Rectangle(HAT_WIDTH, HAT_HEIGHT/2)
    hat_base.set_position(
        SNOWMAN_X_POS - HAT_HEIGHT/1.5,
        offset+(1.5*TOP_RADIUS)
    )
    hat_base.set_color(HAT_BASE_COLOR)
    add(hat_base)
    
    
""" Main Harness """

create_snowman()