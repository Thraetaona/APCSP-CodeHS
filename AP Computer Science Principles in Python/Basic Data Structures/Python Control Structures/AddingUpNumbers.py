"""
This program will add up numbers from 
the user until they enter the sentinel
value, and at the end will print the
total sum. 
"""
SENTINEL = -1

sum = 0

while True:
	num = int(input("Enter a number: "))
	if num == SENTINEL:
		break
	sum += num

print("The total was: " + str(sum))