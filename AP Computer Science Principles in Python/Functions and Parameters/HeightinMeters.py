INCHES_TO_CM = 2.54
CM_TO_METERS = 0.01
FEET_TO_INCHES = 12

# Enter your code here
def convert_height_to_meters(feet, inches):
    height = feet * FEET_TO_INCHES * INCHES_TO_CM
    height = height + (inches * INCHES_TO_CM)
    height = height * CM_TO_METERS
    print(height)
    
convert_height_to_meters(5, 4)
convert_height_to_meters(6, 2)