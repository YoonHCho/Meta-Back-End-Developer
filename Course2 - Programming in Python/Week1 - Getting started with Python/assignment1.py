# Using explicit type conversion, change the following
# inputs so the types match with the following below
#
# name = type string
# age = type int
# height = type float
# loyalty = type boolean

# Modify the line below
name = input('What is your name? ')

print(f"Type of name variable is: {type(name)}. It should be <class 'str'>")

# Modify the line below
age = int(input('What is your age? '))

print(f"Type of age variable is: {type(age)}. It should be <class 'int'>")

# Modify the line below
height = float(input('What is your height in meters? '))

print(
    f"Type of height variable is: {type(height)}. It should be <class 'float'>")

# Modify the line below
loyalty = bool(input('Are you part of our loyalty program? '))

print(
    f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")
