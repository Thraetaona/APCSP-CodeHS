"""
This program reads a password from the 
user and checks if the password is
the same. If the guess is part
the password, we will say it is close.
"""

# What happens when you enter abc123?
# What happens when you enter abc?
# What happens when you enter abc1234?

secret_password = "abc123"
password = input("Password: ")
if password == secret_password:
	print("Passwords match.")
# in notation looks to see if password is found 
# anywhere in the secret password.
elif password in secret_password:
    print("Close!")
else:
	print("Passwords don't match.")