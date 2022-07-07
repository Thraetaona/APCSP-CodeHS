"""
This program helps us divide a large number
of people into groups. We tell it how many
total people there are, and how many people
there are per group, and we figure out
how many groups there are, and how many
are left over. 
"""

people = int(input("Num people: "))
people_per_group = int(input("People per group: "))


# We must use integer division to make sure the result
# is an integer
groups = people // people_per_group

# The % operator helps us find the remainder
people_left = people % people_per_group

print("There are " + str(groups) + " groups " + \
	"with " + str(people_left) + " left over.")