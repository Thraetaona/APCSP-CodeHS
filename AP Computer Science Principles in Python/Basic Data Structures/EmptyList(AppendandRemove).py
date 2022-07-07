# Enter your code here

test = list([])


test.append(int(3))
test.append(str("hello"))
test.append(bool(False))


for item in test:
    print(item)


test.remove(str("hello"))
test.remove(bool(False))


print(str(test))