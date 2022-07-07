import random

count = 0

while True:
	first = random.randint(1, 6)
	second = random.randint(1, 6)
	
	count += 1
	print("Rolled: " + str(first) + " " + str(second))
	
	if (first == 1 == second):
		break
	
		

print("It took you " + str(count) + " rolls to get snake eyes.")