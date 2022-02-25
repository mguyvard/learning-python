checking_clients = True
prompt = "\nHello, what sandwich would you like? Choose from the following:\n\
           \n[1]--Egg sandwich\n[2]--Seafood sandwich\n[3]--Roast beef sandwich\
           \n[4]--Grilled cheese\n[5]--Ham sandwich\n[6]--Nutella sandwich\
           \n[7]--Grilled chicken sandwich\nType number here:___"    
sandwiches = {"1":"egg sandwich", "2":"seafood sandwich", 
              "3":"roast beef sandwich", "4":"grilled cheese",
              "5":"ham sandwich", "6":"nutella sandwich", 
              "7":"grilled chicken sandwich"
              }          

while checking_clients:
    question = input(prompt)
    approval = input(f"Ok. You chose {sandwiches[question]}. It will be ready "
                     "in a moment. Type 'ok' to proceed:___")
    while approval != "ok":
        correction = input("Sorry, type 'ok' to proceed, please: ")
        if correction == "ok":
            approval = "ok"
    next = input(f"Here is your {sandwiches[question]}. Thank you!\n\n\
                 Next? (yes or no, please) __")
    if next == "no":
        checking_clients = False
    