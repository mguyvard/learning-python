import json

filename = 'favourite_number.json'
    
def get_new_number():
    name = input("What is your favorite number?__")
    with open(filename, 'w') as f:
        json.dump(name, f) 


def get_stored_number():
    filename = 'favourite_number.json'
    try:
        with open(filename) as f:
            answer = json.load(f)
    except FileNotFoundError:
        return False
    else:
        return answer
    

def favorite_number():
    print("\nHello, Jack!")
    if get_stored_number():
        print(f"I know your favorite number. It's {get_stored_number():}!")
    else:
        get_new_number()
        get_stored_number()
        print(f"You said your favorite number is {get_stored_number()}!")
              

favorite_number()
