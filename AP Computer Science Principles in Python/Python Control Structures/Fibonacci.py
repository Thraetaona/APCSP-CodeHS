MAX = 1000

n1, n2 = 1, 1
nth = 1

while not nth > MAX:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
print(n1)