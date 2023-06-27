'''
Introduction
In this exercise, you will be checking the accuracy of a string input to a given function against some conditions.
You will be writing two functions. The first function will check if the length of the input string is within a specific
limit of words and characters. The second function will check if the basic grammar of the string is well-defined.

Goal
Learn how to create test cases for a given block of code using PyTest.

Objectives
Ensure the string variables that will be passed as arguments to the code are within a specified length and have a well-defined structure.

Instructions
Step 1: Open the test_spellcheck.py file inside the project folder.

Step 2: Import pytest and spellcheck module.

Step 3: Comment out the beta variable using # symbol for now.

Step 4: Next, complete the test_length() and test_struc() functions. These two functions use input_value to check if the functions
defined in spellcheck behave correctly.

Step 5: In test_length() function, you must add two assert statements. In each assert statement you first need to call the required
function from the spellcheck file that you imported, and then check against some conditions.

For example, the format will be similar to:

assert spellcheck.some_function(input_value) against some condition

5.1 Add the first assert statement over function word_count() from the main code which asserts that the returned value is less than 10.

5.2 Add the second assert statement over function char_count() from the main code which asserts that the returned value is less than 50.

Step 6: In the second function test_struc(), you must add two assert statements. The first assert statement checks if the first character
is in upper case. The second assert statement checks if the sentence or the string variable passed ends with a dot (“.”)

6.1 Add the first assert statement over function first_char() from the main code. Now call a built-in function isupper() directly over it,
such as function_name.isupper().

isupper() function returns True if it is called over an upper-case character and False if called over a lower-case character. For example,
"A".isupper() return True and "a".isupper() returns False.

6.2 Add the second assert statement over the function last_char() from the main code and compare it to “.”

Step 7: Save the files.

Step 8: Open the terminal to execute the files.

Step 9: Run the code using the following command (within the  project directory):

python3 -m pytest fileName.py


Step 10:  Both the tests should pass in this case.

Bonus step: Pass the variable beta instead of alpha in all four of the functions. The result should now show one passed and one failed test.  

Tips
Common mistakes made in this process can include the following:

Forgetting to import the pytest and main code file.

Not passing the variable names correctly.
'''
# ***************************** CODING STARTS *****************************
'''
Import statements:
    1. Import pytest and spellcheck modules
'''
### WRITE IMPORT STATEMENTS HERE
import pytest
import spellcheck

# String variables to be tested
alpha = "Checking the length & structure of the sentence."
# beta = "This sentence should fail the test"

# Do not delete this function. You may change the value assigned to input to test different inputs to your test functions.
@pytest.fixture
def input_value():
    input = alpha
    return input

# First test function test_length()
def test_length(input_value):
    """ Tests whether a string has fewer than 10 words and fewer than 50 chars.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string has fewer than 10 words
        2. Use an assert statement to check the given string has fewer than 50 chars

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    ### WRITE SOLUTION CODE HERE
    assert spellcheck.word_count(input_value) < 10
    assert spellcheck.char_count(input_value) < 50

    # raise NotImplementedError()

# Second test function test_struc()
def test_struc(input_value):
    """ Tests whether a string begins with a capital letter and ends with a period.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string begins with a capital letter
        2. Use an assert statement to check the given string end with a period ('.')

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """
    ### WRITE SOLUTION CODE HERE
    assert spellcheck.first_char(input_value).isupper()
    assert spellcheck.last_char(input_value) == '.'

    # raise NotImplementedError()

# Run these tests with `py -m pytest assignment2.py`