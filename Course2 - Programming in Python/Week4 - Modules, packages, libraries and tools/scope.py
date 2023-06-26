def d():
    animal = 'elephant'
    def e():
        nonlocal animal
        animal = 'giraffe'
        print(f'Inside nested function: {animal}')

    print(f'Before calling function: {animal}')
    e()
    print(f'After nested function: {animal}')

animal = 'camel'
d()
print(f'Global animal: {animal}')