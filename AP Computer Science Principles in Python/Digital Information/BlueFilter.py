# Constants for the image
IMAGE_URL = "https://codehs.com/uploads/c709d869e62686611c1ac849367b3245"
IMAGE_WIDTH = 280
IMAGE_HEIGHT = 200

image = Image(IMAGE_URL)
image.set_position(70, 70)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)

#################################################
# Write your function here. Loop through each pixel
# and set each pixel to have a zero blue value.
#################################################
# Constants for the image
IMAGE_URL = "https://codehs.com/uploads/c709d869e62686611c1ac849367b3245"
IMAGE_WIDTH = 280
IMAGE_HEIGHT = 200

image = Image(IMAGE_URL)
image.set_position(70, 70)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)


# Write this function!
def invert_pixel(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    
    red = red
    green = green
    blue = 0
    
    return (red, green, blue)

# Applies invert filter to picture
def remove_blue():
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_pixel(x,y)
            new_colors = invert_pixel(pixel)
            image.set_red(x, y, new_colors[0])
            image.set_green(x, y, new_colors[1])
            image.set_blue(x, y, new_colors[2])
            
# Give the image time to load
print("Removing Blue Channel ....")
print("Might take a minute....")
timer.set_timeout(remove_blue, 1000)