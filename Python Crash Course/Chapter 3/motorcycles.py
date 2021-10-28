motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles[0] = 'harley'
print(motorcycles)
moto = []
moto.append('italika')
moto.append('yamaha')
moto.append('ktm')
print(moto)
moto.insert(2, 'elektra')
print(moto)
del moto[2]
print(moto)
motos = ['honda', 'yamaha', 'suzuki']
print(motos)
popped_motorcycle = motos.pop()
print(motos)
print(popped_motorcycle)
last_owned = motos.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
first_owned = motos.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me!!!")