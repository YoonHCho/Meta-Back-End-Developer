'''
Instructions
Step 1: Open the comprehensions.py file

Step 2: Implement the to_mod_list() function by using the map() function to apply mod() to all elements within employee_list.
Assign the result of it to a new variable called map_emp. Convert map_emp to a list and return it.

The mod() function returns a string value for example such as “Lisa_Cold Storage” from the dictionary passed to it.

Step 3: At this point you should have a list of the values such as: “Lisa_Cold Storage” mentioned above. But that is no good
for a username with the whitespace present in it. Implement the generate_usernames() method by using list comprehension and
the replace()  over mod_list to replace all spaces (" ") with underscores ("_"). Return the resulting list.

Step 4: We want to create a dictionary that stores employees' first initials and IDs. Implement map_id_to_initial() by using
dictionary comprehension over the employee_list to create a dictionary where each key is the first letter of an employee's name
and the value is the employee's ID.

Step 5: Run the script by opening the terminal and executing the command
'''

# Input data: List of dictionaries
employee_list = [
    {"id": 12345, "name": "John", "department": "Kitchen"},
    {"id": 12456, "name": "Paul", "department": "House Floor"},
    {"id": 12478, "name": "Sarah", "department": "Management"},
    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
    {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function. Do not change this.


def mod(employee_list):
    temp = employee_list['name'] + "_" + employee_list["department"]
    return temp


def to_mod_list(employee_list):
    """ Modifies the employee list of dictionaries into list of employee-department strings

    [IMPLEMENT ME] 
       1. Use the map() method to apply mod() to all elements in employee_list

    Args:
       employee_list: list of employee objects

    Returns:
       list - A list of strings consisting of name + department.
    """
    # WRITE SOLUTION CODE HERE
    map_emp = list(map(mod, employee_list))
    return map_emp

    raise NotImplementedError()


def generate_usernames(mod_list):
    """ Generates a list of usernames 

    [IMPLEMENT ME] 
       1. Use list comprehension and the replace() function to replace space
          characters with underscores

       List comprehension looks like:
       list = [ function() for <item> in <list> ]

       The format for the replace() function is:

       test_str.replace(“a”, “z”) # replaces every “a” in test_str with “z”

    Args:
       mod_list: list of employee-department strings

    Returns:
       list - A list of usernames consisting of name + department delimited by underscores.
    """
    # WRITE SOLUTION CODE HERE
    modifiedUsernames = [mod.replace(' ', '_') for mod in mod_list]
    return modifiedUsernames

    raise NotImplementedError()


def map_id_to_initial(employee_list):
    """ Maps employee id to first initial

    [IMPLEMENT ME] 
       1. Use dictionary comprehension to map each employee's id (value) to the first letter in their name (key)

       Dictionary comprehension looks like:
       dict = { key : value for <item> in <list> }

    Args:
       employee_list: list of employee objects

    Returns:
       dict - A dictionary mapping an employee's id (value) to their first initial (key).
    """
    # WRITE SOLUTION CODE HERE
    dictionEmp = {ele["name"][0]: ele["id"] for ele in employee_list}
    return dictionEmp

    raise NotImplementedError()


def main():
    mod_emp_list = to_mod_list(employee_list)
    print("Modified employee list: " + str(mod_emp_list) + "\n")

    print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

    print(f"Initials and ids: {map_id_to_initial(employee_list)}")


if __name__ == "__main__":
    main()
