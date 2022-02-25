responses = {}
polling_active = True
check = True

while polling_active: 
    name = input("\nWhat is your name: ")
    response = input("Where would you like to visit? ")
    responses[name] = response   
    repeat = input("\nWould you like to let someone answer? (yes/no) ")
    while (repeat != "yes" and repeat != "no"):
        repeat = input("\nWrong answer. Answer yes or no, please: ")
        if repeat == "no":
           polling_active = False
    if repeat == "no":
        polling_active = False
             
print("\n----Poll results----")
for key, value in responses.items():
    print(f"{key.title()} wants to visit {value.title()}")
    