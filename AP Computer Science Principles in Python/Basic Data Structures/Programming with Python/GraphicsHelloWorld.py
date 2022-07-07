# Print Hello World to the screen

cent_x = get_width()/2
cent_y = get_height()/2


txt = Text("Hello   World..!")
txt.set_position(cent_x, cent_y)

new_x = cent_x - txt.get_x()
print(cent_x)
print(txt.get_x())
txt.set_color(Color.blue)
txt.set_font("20pt Arial")
add(txt)