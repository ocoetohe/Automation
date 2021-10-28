pizzas = ['salami', 'mexicana', 'camaron']
friend_pizza = pizzas[:]
pizzas.append('pastor')
friend_pizza.append('hawaiana')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())
print("\nMy friend's favorite pizzas are:")
for friend in friend_pizza:
    print(friend.title())