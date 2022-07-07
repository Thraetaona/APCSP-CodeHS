def key_down(event):
    if event.key == "ArrowLeft":
        if not ((circ.get_radius()-10) < 10):
            circ.set_radius(circ.get_radius()-10) 
    if event.key == "ArrowRight":
        if not ((circ.get_radius()+10) > 200):
            circ.set_radius(circ.get_radius()+10)

circ = Circle(100)
circ.set_position(250, 250)
add(circ)


add_key_down_handler(key_down)