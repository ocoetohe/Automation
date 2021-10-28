animals = ['panda', 'snake', 'horse', 'tiger', 'dog', 'cat', 'eagle', 'ant']
print("\nThe first three pets in the list are:")
for animal in animals[0:3]:
    print(animal.title())
print("\nThe pets in the middle are:")
for animal in animals[2:6]:
    print(animal.title())
print("\nThe last three pets in the list are:")
for animal in animals[-3:]:
    print(animal.title())