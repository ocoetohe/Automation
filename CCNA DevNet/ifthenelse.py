from __future__ import print_function

name = input('Please tell me your name: ')
rawAge = input('Please tell me your age: ')
age = int(rawAge)

if age >= 21:
    print(name, 'you are allowed in!')
    print('What would you like to drink?')

elif age >= 18:
    print('You are allowed in!')
    print('But you are not allowed to drink, please feel free to dance!')

else:
    print('Unfortunately',name,'you are your are not allowed in!')
