# read petnames.txt and select a random name for your pet
import random

with open('petnames.txt', 'r') as file:
    fileContent = file.read()
    fileList = fileContent.split('\n')
    randomIndex = int(random.random() * len(fileList))
    # print(random.choice(fileList))
    print(fileList[randomIndex])
