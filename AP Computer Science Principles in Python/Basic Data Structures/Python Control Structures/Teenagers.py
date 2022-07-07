# Enter your code here

age = int(input("What is your age?"))

is_teenager = bool((age >= 13) and (age <= 19))

if is_teenager:
    print("Yes, you are a teenanger")
else:
    print("No, you are not a teenager")