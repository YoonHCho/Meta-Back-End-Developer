# Given implementations of some string-related methods. 
# DO NOT CHANGE THIS FILE

def word_count(sentence):
    # Function to check the number of words. Returns the word count in string.
    words = len(sentence.split())
    print(words)
    return words

def char_count(sentence):
    # Function to check the number of characters. Returns the character count in string.
    chars = len(sentence)
    print(chars)
    return chars

def first_char(sentence):
    # Function to check the first character using the string index. Returns the first character in string.
    first = sentence[0]
    return first

def last_char(sentence):
    # Function to check the last character using the string index. Returns the last character in string.
    last = sentence[-1]
    return last