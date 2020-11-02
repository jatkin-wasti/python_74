# We are asking the user for their information and storing it in the 'name', 'dob', and 'age' variables
name = input("Please enter your full name:  ")
dob = input("Please enter your date of birth in DD/MM/YYYY format:  ")
age = input("Please enter your age:  ")
# We are then displaying the information they gave to us in a natural sounding sentence
print(f"Hi, {name}! Your date of birth is {dob}, so you are {age} years old!")
# Finally, we display the data types of the variables created
print(f"The data types of the following variables are as follows.\n"
      f"name: {type(name)}\n"
      f"dob: {type(dob)}\n"
      f"age: {type(age)}")