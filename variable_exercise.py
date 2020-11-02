name = input("Please enter your full name:  ")
dob = input("Please enter your date of birth in DD/MM/YYYY format:  ")
age = input("Please enter your age:  ")
print(f"Hi, {name}! Your date of birth is {dob}, so you are {age} years old!")
print(f"The data types of the following variables are as follows.\n"
      f"name: {type(name)}\n"
      f"dob: {type(dob)}\n"
      f"age: {type(age)}")