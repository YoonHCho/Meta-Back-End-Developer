dict1 = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
print(dict1[1])
dict1[2] = 'Mint Tea'
print(dict1)
del dict1[3]
print(dict1)

dict2 = {1: 'Test', 'Name': 'Jim'}
dict2[2] = 'Test 2'
print(dict2['Name'])
print(dict2)

for key, value in dict2.items():
    print(f"key: {key} and the value: {value}")
