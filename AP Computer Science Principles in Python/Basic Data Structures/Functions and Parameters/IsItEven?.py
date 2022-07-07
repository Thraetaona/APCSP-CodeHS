SENTINEL = 0

def is_even(num):
	is_even_number = ((num % 2) == 0)
	return is_even_number
	
val = 1
while (val != SENTINEL):
    val = input("Enter a number:")
    is_even_number = is_even(val)
    
    if (is_even_number):
        print("Even")
    else:
        print("Odd")
    

print("Done!")