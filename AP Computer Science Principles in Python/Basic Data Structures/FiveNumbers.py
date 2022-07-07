num_list = list([])
summation = 0
for i in range(5):
    num = input("Number: ")
    num_list.append(num)
    print(str(num_list))
    summation += num
    
print(summation)