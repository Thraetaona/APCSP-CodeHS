# This program reads a number from the
# user and prints out whether it is
# even or odd using the modulus operator.

num = int(input("Number: "))
if num % 2 == 0:
	print("Number is even.")
else:
	print("Number is odd.")