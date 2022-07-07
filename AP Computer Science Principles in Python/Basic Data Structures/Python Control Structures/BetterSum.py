# Enter your code here
first = int(input("First? "))
second = int(input("Second? "))

summ = 0
for i in range(first, second+1):
    summ += i
    
print(summ)