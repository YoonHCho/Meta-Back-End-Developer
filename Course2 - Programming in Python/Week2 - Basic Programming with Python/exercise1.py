# Exercise: Exceptions in Python

# IndexError
items = [1, 2, 3, 4, 5]

try:
    item = items[6]
    print(item)
except IndexError as e:
    print(e, "Item does not exist in the list")

# ZeroDivisionError


def divide_by(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return (f"{e}, cannot divide by zero")
    except Exception as e:
        return (e, "something went wrong")


ans = divide_by(40, 0)
print(ans)

# FileNotFoundError
try:
    with open('file_does_not_exist.txt', 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print(e, 'The file could not be found')
