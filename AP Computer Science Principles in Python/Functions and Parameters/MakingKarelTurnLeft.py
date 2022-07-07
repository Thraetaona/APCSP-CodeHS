# This program creates Karel without any of the builtin Karel commands,
# it makes Karel from scratch using Python.
#
# In this program, we build Karel's World in Python.

NUM_STREETS = 4
NUM_AVES = 4
POINT_SIZE = 3
WORLD_WIDTH = 275
WORLD_HEIGHT = 275
set_size(WORLD_WIDTH, WORLD_HEIGHT)

STREET_HEIGHT = WORLD_HEIGHT // NUM_STREETS
AVE_WIDTH = WORLD_WIDTH // NUM_AVES
PAUSE_TIME = 1000

# Constants for creating Karel
KAREL_IMG_URL = "https://codehs.com/uploads/9657058ec012105e0c5548c917c29761"
KAREL_SIZE = STREET_HEIGHT
# Starting position for Karel
X_POS = 0 
Y_POS = WORLD_HEIGHT - KAREL_SIZE

# represents angles of rotation
EAST = 0
SOUTH = math.radians(90)
WEST = math.radians(180)
NORTH = math.radians(270)

# Creates Karel's world with Karel in the bottom left corner facing east.
def setup_world():
    global direction, karel
    # Add the points to the grid
    for street in range(NUM_STREETS):
        for ave in range(NUM_AVES):
            x_center = ave * AVE_WIDTH + AVE_WIDTH / 2
            y_center = street * STREET_HEIGHT + STREET_HEIGHT / 2
            dot = Circle(POINT_SIZE, x_center, y_center)
            add(dot)    
    
    # Add Karel to the grid
    karel = Image(KAREL_IMG_URL)
    karel.set_position(X_POS, Y_POS)
    karel.set_size(KAREL_SIZE, KAREL_SIZE)
    add(karel)

    # Variables to keep track of karel and karel's direction
    # Set Karel's initial direction
    direction = EAST


def turn_left():
    global karel, direction
    
    if direction == EAST:
        direction = NORTH
    elif direction == WEST:
        direction = SOUTH
    elif direction == NORTH:
        direction = WEST
    elif direction == SOUTH:
        direction = EAST
    else:
        print("Error: Karel's Direction is not properly set.")
        direction = EAST 
    
    karel.set_rotation(direction)
    
    

timer.set_interval(turn_left, PAUSE_TIME)
setup_world()