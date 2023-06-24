menu = ['espresso', 'mocha', 'latte', 'cappuccino', 'cortado', 'americano']


def startsWithC(string):
    if string.startswith('c'):
        return string


filterC = filter(startsWithC, menu)
print('FILTER: ', list(filterC))

mapC = map(startsWithC, menu)
print('MAP: ', list(mapC))
######################

a = [[96], [96]]
b = map(str, a)
print(list(map(str, a)))
c = list(b)
print(list(b))
d = ''.join(c)
print(d)

print(''.join(list(map(str, a))))
