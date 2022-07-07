my_tuple = (0, 1, 2, "hi", 4, 5)

# Your code here...

x = my_tuple[0:3]
y = my_tuple[4:6]

my_tuple = x + (3,) + y

print(my_tuple)