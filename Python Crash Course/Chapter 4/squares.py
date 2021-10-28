squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"\nEl numero minimo de la lista es: {min(digits)}")
print(f"El numero maximo de la lista es: {max(digits)}")
print(f"La suma de todos los numeros de la lista es: {sum(digits)}\n")

potencias = [potencia**2 for potencia in range(1, 101)]
print(potencias)