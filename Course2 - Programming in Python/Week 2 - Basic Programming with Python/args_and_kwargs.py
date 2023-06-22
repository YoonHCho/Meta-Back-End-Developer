def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum


print('sum_of: ', sum_of(4, 5, 6))


def sum_of_kwargs(**kwargs):
    sum = 0
    for k, v in kwargs.items():
        sum += v
    return sum


print('sum_of_kwargs: ', sum_of_kwargs(coffee=1.99, tea=1.46, boba=2.99))
