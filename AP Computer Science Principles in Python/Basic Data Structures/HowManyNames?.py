name_amount = int(input("How many names do you have? "))
namelist = []
index = 0
for i in range (name_amount):
    name = input("Name: ")
    namelist.append(name)
    index += 1
print("First name: " + namelist[0])
print("Middle names: " + str(namelist[1:-1]))
print("Last name: " + namelist[-1])