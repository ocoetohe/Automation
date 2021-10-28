million = []
for value in range(1, 1001):
    million.append(value)
print(million)
print(f"\nEl numero minimo de la lista es: {min(million)}")
print(f"El numero maximo de la lista es: {max(million)}")
print(f"La suma de numeros de la lista es: {sum(million)}\n")

for oddn in range(1, 21, 2):
    print(oddn)

for numt in range(3, 31, 3):
    print(numt)

cubes = []
for value in range(1, 11):
    cubes.append(value**3)
print(cubes)

cubescomp = [value**3 for value in range(1, 11)]
print(cubescomp)