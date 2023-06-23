with open('sample.txt', 'r') as file:
    # print(file.read(34))
    # print(file.readline())
    # data = file.readlines()
    # for line in data:
    #     print(line.strip())

    # when you use 'with open' as, it returns a list as a default, this case file variable
    for line in file:
        print(line.strip())
