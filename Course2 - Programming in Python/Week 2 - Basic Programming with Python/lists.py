list1 = [1, 2, 3, 4, 5]

list2 = ['A', 'B', 'C']

list3 = ['Hello', 1, True, 13.23]

list4 = [1, [2, 3, 4], 5, 6]

# print(list1)
# print(*list1)
list1.insert(len(list1), 6)
list1.append(7)
list1.extend([8, 9, 10])
print(list1)
list1.pop(-1)
del list1[0]
print(list1)
