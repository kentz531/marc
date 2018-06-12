# Creating a List

# Index 0, 1, 2, 3
digits = [1, 3, 3, 5, 6]
apples = ['Fuji', 'Gala', 'Green', 'American']
combined = ["Marc", 28, True]

apples = []

apples.append('Fuji')
apples.append('Gala')
apples.append('Green')

apples = list(('Fuji', 'Gala', 'Green', 'American'))

# COMMON METHODS FOR LIST
apple = apples[1]
digits.pop(0)
len(apples)

for element in apples:
    print(element)

new_list = digits + apples
print(new_list)

digits.extend(apples)
print(digits)

# LIST to tuple and vice versa
apples = ['Fuji', 'Gala', 'Green', 'American']
print(type(apples))

apples = tuple(apples)
print(type(apples))

apples = ('Fuji', 'Gala', 'Green', 'American')
print(type(apples))

apples = list(apples)
print(type(apples))
