#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

#requested_toppings = []

#if requested_toppings:
#    for req_topping in requested_toppings:
#        print(f"Adding {requested_toppings}...")
#    print("\nFinished making your pizza!!!")
#else:
#    print("Are you sure you want a plain pizza?")
#
#for req_topping in requested_toppings:
#    if req_topping == 'green peppers':
#        print("Sorry, we are out of green peppers right now.")
#    else:
#        print(f"Adding {req_topping.title()}...")

#print("\nFinished making your pizza!!!")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza")
