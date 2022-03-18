def check_string(input_value):
    """Return True if input_value is a string and False otherwise"""
    try:
        input_value = int(input_value)
    except ValueError:
         return True
    else:
        return False
   
while True:
    number1 = input("Enter a 1st number (or 'q' to quit):__")
    while check_string(number1) and number1 != 'q':
        number1 = input("Not a number. Type a 1st number (or 'q' to quit):__")
        check_string(number1)
    if number1 == 'q':
        break
    else:
        number2 = input("Enter a 2nd number (or type 'q' to quit):__")
        while check_string(number2) and number2 != 'q':
            number2 = input("Not a number. Type a 2nd number (or 'q' to quit):__")
            check_string(number2)
        if number2 == 'q':
            break
        else:
            answer = int(number1) + int(number2)
            print(f"The sum of {number1} and {number2} is {answer}")
            

