# your function should return the maximum value in `my_list`
def max_int_in_list(my_list):
    maximum = my_list[0]
    
    for i in range(0, len(my_list)):
        if my_list[i] >= maximum:
            maximum = my_list[i]
    
    return maximum