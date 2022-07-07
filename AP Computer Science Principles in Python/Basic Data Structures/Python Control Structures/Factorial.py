# Enter your code here
first = int(input("Number? "))

summ = 1
for i in range(0, first):
    summ *= (first-i)
    
print(summ)