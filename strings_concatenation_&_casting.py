# What is concatenation
# Assigning values to variables
first_name = "James"
middle_name = "'Danger'"
last_name = "Bond"
age = 37  # This is an int so it can't be concatenated without casting it as a string

# This prints all of the names on separate lines but it wastes 3 lines when it could be written on 1
print(first_name)
print(middle_name)
print(last_name)

# These both print all of the names on the same line with spaces between the names
print(first_name + ' ' + middle_name + ' ' + last_name)
print(first_name, middle_name, last_name)

# Casting is used to use one data type as if it was another data type
print(first_name + ' ' + middle_name + ' ' + last_name + ' is ' + str(age) + ' years old.')
num_as_string = "007"  # This string contains a number but we may want to use it as an int
print(7 + int(num_as_string))  # Therefore we can cast it as an int to use it like one
