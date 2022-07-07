# this function should return the number of words that contain "owl"!
indices = list([])

def owl_count(text):
    
    text_list = text.split()
    
    counter = 0
    
    for i in range(0, len(text_list)):
        if "owl" in text_list[i]:
            counter += 1
            indices.append(i)
    return counter
    
text = str(input("Enter some text: "))
x = owl_count(text)
print("There were "+ str(x) +" words that contained \"owl\".")
print("They occurred at indices: " + str(indices))