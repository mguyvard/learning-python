prompt = "How old are you." 
prompt += "\n(Enter quit to exit the program): "

age_string = input(prompt)
while age_string != "quit":
    age = int((age_string))
    if age < 3: 
        print("Your ticket is free.")
    elif age < 12:
        print("Your ticket costs 10 dollars")
    else:
        print("Your ticket costs 15 dollars")   
    age_string = input(prompt)
    
print("\nThank you. Goodbye!")