# Constants for the image
IMAGE_URL = "https://codehs.com/uploads/e07cd01271cac589cc9ef1bf012c6a0c"
IMAGE_WIDTH = 280
IMAGE_HEIGHT = 200
DARKENING_FACTOR = 50
MIN_PIXEL_VALUE = 0

image = Image(IMAGE_URL)
image.set_position(70, 70)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)



# Write this function!
def darken_filter(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    red = red - DARKENING_FACTOR
    green = green - DARKENING_FACTOR
    blue = blue - DARKENING_FACTOR
    
    return (red, green, blue)

# Applies invert filter to picture
def change_picture():
    for x in range(0, int(image.get_width()/2)):
        for y in range(image.get_height()):
            pixel = image.get_pixel(x,y)
            new_colors = darken_filter(pixel)
            image.set_red(x, y, new_colors[0])
            image.set_green(x, y, new_colors[1])
            image.set_blue(x, y, new_colors[2])
# Give the image time to load
print("Making Darker....")
print("Might take a minute....")
timer.set_timeout(change_picture, 1000)

print("done")