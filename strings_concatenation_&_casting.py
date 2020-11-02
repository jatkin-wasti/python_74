# # What is concatenation
# # Assigning values to variables
# first_name = "James"
# middle_name = "'Danger'"
# last_name = "Bond"
# age = 37  # This is an int so it can't be concatenated without casting it as a string
#
# # This prints all of the names on separate lines but it wastes 3 lines when it could be written on 1
# print(first_name)
# print(middle_name)
# print(last_name)
#
# # These both print all of the names on the same line with spaces between the names
# print(first_name + ' ' + middle_name + ' ' + last_name)
# print(first_name, middle_name, last_name)
#
# # Casting is used to use one data type as if it was another data type
# print(first_name + ' ' + middle_name + ' ' + last_name + ' is ' + str(age) + ' years old.')
# num_as_string = "007"  # This string contains a number but we may want to use it as an int
# print(7 + int(num_as_string))  # Therefore we can cast it as an int to use it like one
#
#
# name = input("Please enter your full name:  ")
# dob = input("Please enter your date of birth in DD/MM/YYYY format:  ")
# age = input("Please enter your age:  ")
# post_code = input("Please enter your post code:  ")
# first_line_address = input("Please enter the first line of your address:  ")
# house_number = input("Please enter your house number:  ")
# print("Your name is " + name + ".\nYour age is " + str(age) +
#                                ".\nYour date of birth is " + dob +
#                                ".\nYour address is " + str(house_number) +
#                                " " + first_line_address + ", " + str(post_code))

# # Declaring strings with double "" and single '' quotes
# single_quotes = 'Single quotes need an escape character (\\) for appostraphes like so: \'Wow!\''
# print(single_quotes)
# double_quotes = "Whereas in double quotes you don't need to use \\ to escape the appostraphe"
# print(double_quotes)

# String slicing, why?
# indexing in python starts at 0 (as it should)
greetings = "Hello World!"
print(greetings[0:5])  # This uses the index to get the first 5 letters
# Indexing is EXCLUSIVE
# This means that it does not use the 5th number that we provided
# instead it returns the characters in indexes 0,1,2,3,4
print(len(greetings))  # This returns the length of a given string

white_spaces = "Lots of spaces at the end                                      "
print(len(white_spaces))
print(len(white_spaces.strip()))  # The strip() function removes all spaces at the end of a string

# The count() method counts the number of times a string is found in another string e.g. how many times the
# word 'the' appears in a book
text = "lots of text blah blah blah"
print(text.count('blah'))  # This returns 3 because there are 3 instances of the string 'blah' in the text string
print(text.replace('blah', '!'))  # This replaces the instances of 'blah' with '!' in the text string
print(text.capitalize())  # This capitalises the first letter in the string
print(f"You can input text here like so: \n {text}")  # This can use variable names to more cleanly input them to the string
