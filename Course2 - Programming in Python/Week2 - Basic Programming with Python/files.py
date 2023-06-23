# creates a new file, if file exists it overwrites it
with open('newfile.txt', 'w') as file:
    file.write("This is a new file created")
    file.writelines(["\nThis is a new line", "\nThis is another line '3'"])

# add a new text to the file that already exists
with open('newfile.txt', 'a') as file:
    file.writelines(["\nI am added", "\nI am added"])

try:
    with open('sample/newfile.txt', 'a') as file:
        file.writelines(["\nI am added", "\nI am added"])
except FileNotFoundError as e:
    print('Error: ', e)
    # prints: Error:  [Errno 2] No such file or directory: 'sample/newfile.txt'
