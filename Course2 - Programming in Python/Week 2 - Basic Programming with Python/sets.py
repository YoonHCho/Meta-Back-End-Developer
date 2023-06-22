# sets do not allow duplicate value

set_a = {1, 2, 3, 4, 5, 5}
set_a.add(6)
set_a.remove(1)
set_a.discard(2)
print(set_a)

set_b = {1, 2, 3, 4, 5}
set_c = {4, 5, 6, 7, 8}

print(set_b.union(set_c))  # {1, 2, 3, 4, 5, 6, 7, 8}
print(set_b | set_c)  # {1, 2, 3, 4, 5, 6, 7, 8}
print(set_b.intersection(set_c))  # {4, 5}
print(set_b & (set_c))  # {4, 5}
# prints the values in set_b that is not included in set_c
print(set_b.difference(set_c))  # OR set_b - set_c
# this prints all the values that does not included in either variables
print(set_b.symmetric_difference(set_c))  # OR set_b ^ set_c
