pizza_toppings = []

prompt = "\nWhat topping do you want to add to your pizza: "
prompt += "\n(Enter quit to leave): "
topping = input(prompt)

while topping != "quit":
    pizza_toppings.append(topping.title())
    print(f"You selected: {topping.title()}")
    prompt = "\nWhat else would you like to add: "
    prompt += "\n(Enter quit to leave): "
    topping = input(prompt)
    if topping == "quit":
        break
if pizza_toppings == []:
    print("\nYou wanted a plain pizza. Here you are.")
else:
    print("\nThe following toppings have been added: ")
    for topping in pizza_toppings:
        print("-",topping.title())
    print("Here you are!" )
print("\nThank you have a great day!")
