# What are data types

# Boolean gives us the outcome in True or False
# a = True
# b = False
# print(a == b)  # This returns False because a and b do not hold the same value
# print(a != b)  #  This returns True because a and b do not hold the same value
# print(a >= b)  # This returns True because True is greater than False in python

greetings = "Hello World!"
print(greetings.lower())  # This returns the lowercase version of the greetings string
print(greetings.isalpha())  # This checks if all characters in the string are letters so the '!' makes it return False
print(greetings.islower())  # This returns false because the entire string is not all lowercase
print(greetings.startswith('H'))  # This checks the first letter of the string to see if it matches the passed character
print(greetings.endswith('!'))  # This returns true because the last character of the string is an '!'

print(bool(None))  # the boolean value of None is False
