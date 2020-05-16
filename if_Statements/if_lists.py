
#Checking for special items:
requested_toppings = ["mushrooms", "peppers", "onions", "cheese"]
print()
for requested_topping in requested_toppings:
    if requested_topping == "peppers":
        print("Sorry, we are out of peppers at the moment. Won't add peppers.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")
print()


#Checking that a list is not empty:
requested_toppings = []
if requested_toppings: #Python returns True if a list contains at least one item, if empty it returns False.
    for requested_topping in requested_toppings:
        if requested_topping == "peppers":
            print("Sorry, we are out of peppers at the moment. Won't add peppers.")
        else:
            print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")


#Using multiple lists:
available_toppings = ["mushrooms", "peppers", "onions", "cheese", "olives", "pepperoni"]

requested_toppings = ["mushrooms", "french fries", "cheese"]

print()
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")