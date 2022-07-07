'''
This program uses the move(dx, dy) command. Move takes 
two paramaters, a delta x and delta y and updates the position
relative to the current position. See the docs tab for 
additional examples under each shape.
'''

# Don't forget to click on the canvas after you run!
# The keys will not register until you click the canvas!
def key_down(event):
    if event.key == "ArrowLeft":
        square.move(-5, 0) 
    if event.key == "ArrowRight":
        square.move(5, 0)
    if event.key == "ArrowUp":
        square.move(0, -5)
    if event.key == "ArrowDown":
        square.move(0, 5)

square = Rectangle(40, 40)
square.set_position(100, 100)
add(square)


add_key_down_handler(key_down)