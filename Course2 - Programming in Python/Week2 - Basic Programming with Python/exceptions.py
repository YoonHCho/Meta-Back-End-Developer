# Handling exceptions

def divide(a, b):
    return a / b


try:
    print(divide(4, 0))
except ZeroDivisionError as e:
    print(e, "Cannot divide by zero")
except Exception as e:  # if the exception was other than zero division error
    print(f"Something went wrong! {e}")
    print(e.__class__)  # <class 'ZeroDivisionError'>
