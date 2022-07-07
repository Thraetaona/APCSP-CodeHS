"""
This constant represents our currency conversion 
rate. Since the value should not change, we
format it as a constant.

To help distinguish constant  values from variables,
we  format constants in all capital letters.
"""
DOLLARS_TO_POUNDS = 0.6462

# This program will convert dollars to pounds

print("This program converts USD to GBP.")
dollars = float(input("USD: "))

# This is how we can convert from dollars to pounds
pounds = dollars * DOLLARS_TO_POUNDS

print("GBP: " + str(pounds))