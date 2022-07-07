import math

# fill in this function to return the distance between the two points!
def distance(first_point, second_point):
    x = abs(first_point[0] - second_point[0])
    y = abs(first_point[1] - second_point[1])
    
    res = math.sqrt(pow(x, 2) + pow(y, 2))
    return res