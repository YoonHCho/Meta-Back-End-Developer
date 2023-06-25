import calendar
import sys

sys.path.insert(1, r'C:\Users\ycho8\Desktop\Coding\Coursera\Meta-Back-End-Developer\Course2 - Programming in Python\Week4 - Modules, packages, libraries and tools\module')
import names


location = sys.path


print('names.names: ', names.names)


print(location)
for i in location:
    print(i)


leapYear = calendar.leapdays(2000, 2050)
print(leapYear)

isLeap = calendar.isleap(2036)
print(isLeap)


print("THERE ARE LEAPYEAR %r; AND ISLEAP %r" % (leapYear, isLeap))
