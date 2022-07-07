# Constants for body
HEAD_RADIUS = 35
BODY_WIDTH = HEAD_RADIUS * 2
BODY_HEIGHT = 60
NUM_FEET = 3
FOOT_RADIUS = (BODY_WIDTH) / (NUM_FEET * 2)

# Constants for eyes
PUPIL_RADIUS = 4
PUPIL_LEFT_OFFSET = 8
PUPIL_RIGHT_OFFSET = 20
EYE_RADIUS = 10
EYE_OFFSET = 14


# Put your function(s) here
def draw_ghost(center_x, center_y, color):
    head = Circle(HEAD_RADIUS)
    head.set_position(center_x, center_y)
    head.set_color(color)
    add(head)
    
    body = Rectangle(BODY_WIDTH, BODY_HEIGHT)
    body.set_position(center_x-(BODY_WIDTH/2), center_y+(HEAD_RADIUS/10))
    body.set_color(color)
    add(body)
    
    left_eye = Circle(EYE_RADIUS)
    left_eye.set_position(center_x-EYE_OFFSET, center_y)
    left_eye.set_color(Color.white)
    add(left_eye)

    right_eye = Circle(EYE_RADIUS)
    right_eye.set_position(center_x+EYE_OFFSET, center_y)
    right_eye.set_color(Color.white)
    add(right_eye)

    left_pupil = Circle(PUPIL_RADIUS)
    left_pupil.set_position(center_x-PUPIL_LEFT_OFFSET, center_y)
    left_pupil.set_color(Color.blue)
    add(left_pupil)

    right_pupil = Circle(PUPIL_RADIUS)
    right_pupil.set_position(center_x+PUPIL_RIGHT_OFFSET, center_y)
    right_pupil.set_color(Color.blue)
    add(right_pupil)
    
    offset = BODY_WIDTH/NUM_FEET
    
    for _ in range(0, NUM_FEET):
        foot = Circle(FOOT_RADIUS)
        foot.set_position(center_x-(offset), center_y+BODY_HEIGHT)
        foot.set_color(color)
        add(foot)
        
        offset -= FOOT_RADIUS*2
                
center_x = get_width()/2
center_y = get_height()/2
draw_ghost(center_x, center_y, Color.red)
draw_ghost(100, 150, Color.green)
draw_ghost(370, 200, Color.black)
draw_ghost(40, 250, Color.orange)
draw_ghost(300, 100, Color.yellow)