def isPalindrome(inputStr):
    endIndex = int(len(inputStr) - 1)
    checkLength = int(len(inputStr) / 2)

    for i in range(len(inputStr)):
        if i == checkLength and i % 2 != 0:
            continue
        if inputStr[i] != inputStr[endIndex - i]:
            return False
    return True


print(isPalindrome('racecar'))  # True
print(isPalindrome('radecar'))  # False
print(isPalindrome('olettelo'))  # True
print(isPalindrome('oleetelo'))  # False
