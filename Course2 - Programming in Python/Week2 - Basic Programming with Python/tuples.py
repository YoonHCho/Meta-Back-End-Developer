my_tuples = (1, 'STRINGS', 4.5, True, 4.5, 4.5)

print(my_tuples[1])
print(my_tuples.count(4.5))  # prints 3 since there are three 4.5 in this tuple
print(my_tuples.index(4.5))  # prints 2
print(my_tuples.index(True))  # prints 2
