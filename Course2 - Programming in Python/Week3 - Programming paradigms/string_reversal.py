# str[start:stop:step]

# str_one = 'reversal'
# new_str = str_one[::-1]
# print(new_str)

# Using recursion
def string_reverse(string):
    if len(string) == 0:
        return string
    else:
        return string_reverse(string[1:]) + string[0]


reversedStr = string_reverse("reversed")
print(reversedStr)
