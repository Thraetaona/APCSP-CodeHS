# All you have to do in this exercise is write a good comment that explains
# what local variables are. You should also give an example of a function
# and what the local variables are, and what the scope is of the variable.

# Local variable is local and its scope is limited within the scope
def add_one(x):
	# The result variable in this function is totally
	# different than the one in the sum function
	result = x + 1
	return result

def sum(x, y):
	result = x + y
	return result
	
x = add_one(8)
print(x)

y = add_one(10)
print(y)

a = sum(10, 20)
print(a)