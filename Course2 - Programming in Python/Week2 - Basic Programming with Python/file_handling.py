# open & close
# file = open('test.txt', mode='r')
# data = file.readline()
# print(data)
# file.close()

# with open, does not need to close the file.
with open('test.txt', mode='r') as file:
    data = file.readline()
    print(data)
