num_list = list([])

for i in range(5):
    num = str(input("Name:"))
    
    num = num.split()
    
    
    num_list.append(num[1])

num_list.sort()
print(num_list)