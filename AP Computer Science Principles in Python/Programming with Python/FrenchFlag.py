# Create a Blue rectangle on left
blue_stripe = Rectangle(get_width()/3, get_height())
blue_stripe.set_color(Color.blue)
blue_stripe.set_position(0, 0)
add(blue_stripe)

# Create a Red rectangle on right
red_stripe = Rectangle(get_width()/3, get_height())
red_stripe.set_color(Color.red)
red_stripe.set_position(get_width()*2/3, 0)
add(red_stripe)