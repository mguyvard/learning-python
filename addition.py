
try:
    number1 = input("Enter a first number:__")
    number1 = int(number1)
except ValueError:
    print("This is not a number")       
else:
    try:
        number2 = input("Enter a second number:__")
        number2 = int(number2)
    except ValueError:
        print("This is not a number")
    else:
        print( number1 + number2)
    

    
