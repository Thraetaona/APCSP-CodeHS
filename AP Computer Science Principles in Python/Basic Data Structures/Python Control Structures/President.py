# Here we write a program to determine
# if someone meets the requirements to 
# become President of the United States.
# They must:
# 1. Be at least 35 years old
# AND
# 2. Be a US Citizen

at_least_thirty_five = False
is_us_citizen = True
can_be_president = at_least_thirty_five and is_us_citizen
print("Can be president: " + str(can_be_president))