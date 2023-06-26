'''
Goal
Use the import statement to import a built-in package in Python.

Use the import statement to call a function present in another Python file.

Objectives
Learn how to use import to bring external code within direct scope of the project.

Instructions:
Step 1: Open the file jsongenerator.py present inside project folder.

Step 2: Import a built-in package called json.

Step 3: Import the following from a file called employee.py:

A function called details

Variables called employee_name, age and title

Step 4: Implement the create_dict() function that returns a dictionary given employee information.

4.1 Create and return a dictionary with three key-value pairs where

keys are string variables - “first_name”, “age” and “title” and their respective values are employee_name,
age and title variables that we have imported from the employee module. Be sure to cast the values to the expected types.

Step 5:

Use a function called dumps() from the json module using dot notation and pass the employee_dict dictionary that we have created to it.
Return its value to a variable named json_object.

The format of the same should look like:

variable = json.dumps(dict)

Step 6: Complete the write_json_to_file() function

6.1 Use a built-in function called open() and pass the output_file argument and “w” to it. Return the value of this function to a variable named newfile.

 6.2 Call a function called write() over this variable newfile. Pass the json_object variable you created in Step 5 inside it.

6.3 Close this file by calling a built-in function close() directly on newfile. You don’t need to pass any arguments here.

Step 7: Save the files.

Step 8: Open the terminal to execute the files.

Step 9: Run the code using the command (within project directory)
'''

'''
Import statements:
    1. Import the built-in json python package
    2. From employee.py, import the details function and the employee_name, age, title variables
'''
### WRITE IMPORT STATEMENTS HERE
import json
from employee import employee_name, age, title, details

def create_dict(name, age, title):
    """ Creates a dictionary that stores an employee's information

    [IMPLEMENT ME]
        1. Return a dictionary that maps "first_name" to name, "age" to age, and "title" to title

    Args:
        name: Name of employee
        age: Age of employee
        title: Title of employee

    Returns:
        dict - A dictionary that maps "first_name", "age", and "title" to the
               name, age, and title arguments, respectively. Make sure that
               the values are typecasted correctly (name - string, age - int,
               title - string)
    """
    ### WRITE SOLUTION HERE
    empInfo = {}
    empInfo['first_name'] = str(name)
    empInfo['age'] = int(age)
    empInfo['title'] = str(title)
    return empInfo

    raise NotImplementedError()

def write_json_to_file(json_obj, output_file):
    """ Write json string to file

    [IMPLEMENT ME]
        1. Open a new file defined by output_file
        2. Write json_obj to the new file

    Args:
        json_obj: json string containing employee information
        output_file: the file the json is being written to
    """
    ### WRITE SOLUTION HERE
    newfile = open(output_file, 'w')
    newfile.write(json_obj)
    newfile.close()
    return None

    raise NotImplementedError()

def main():
    # Print the contents of details() -- This should print the details of an employee
    details()

    # Create employee dictionary
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    '''
    Use a function called dumps from the json module to convert employee_dict
    into a json string and store it in a variable called json_object.
    '''
    ### WRITE YOUR CODE BY MODIFYING THE LINE BELOW
    # In the line below replace the None keyword with your code.
    # The format should look like: variable = json.dumps(dict)
    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))

    # Write out the json object to file
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()