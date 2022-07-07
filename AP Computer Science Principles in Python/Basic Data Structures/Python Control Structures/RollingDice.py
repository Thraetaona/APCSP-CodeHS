# Enter your code here
first = int(input("First die?"))
print(first)
second = int(input("Second die?"))
print(second)

rolled_doubles = bool((first == second))

print("Rolled doubles?" + str(rolled_doubles))