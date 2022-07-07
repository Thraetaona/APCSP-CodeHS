STARTING_ITEMS_IN_INVENTORY = 20

num_items = STARTING_ITEMS_IN_INVENTORY
# Enter your code here


while (STARTING_ITEMS_IN_INVENTORY != 0):
    
    print("We have "+ str(STARTING_ITEMS_IN_INVENTORY) + " items in inventory.")    
    num = int(input("How many would you like to buy? "))
    if num > STARTING_ITEMS_IN_INVENTORY:
        print("There is not enough in inventory for that purchase.")
    else:
        STARTING_ITEMS_IN_INVENTORY -= num
    
    if STARTING_ITEMS_IN_INVENTORY != 0:
        print("Now we have " + str(STARTING_ITEMS_IN_INVENTORY) + " left.")
        
print("All out!")