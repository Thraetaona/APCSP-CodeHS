def minVal(x, y):
	# Python's style of the 'select' or ternary operator.
	minVal = (y if (x >= y) else x)
	return minVal
	

x = minVal(10, 14)
print("The min is " + str(x))

x = minVal(2, 6)
print("The min is " + str(x))

x = minVal(1, 1)
print("The min is " + str(x))