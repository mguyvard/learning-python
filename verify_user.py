import json

def get_stored_username(name):
    """Get stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            contents = json.load(f)
    except FileNotFoundError:
        with open(filename, 'w') as f:
            contents = json.load(f)
            contents.append(name)
            return [""]
    else:
        return contents
            
def get_new_username(name):
    """Stores the user's name"""
    filename = 'username.json'

    with open(filename, 'w') as f:
        json.dump(name, f)
    
def greet_user():
    """Greet the username by name"""
    name = input("Hello, what is your name?__ ").lower()
    if name in get_stored_username(name):
        print(f"Welcome back, {name.title()}!")
    else:
        get_new_username(name)
        print(f"The next time you log in we'll remember you, {name.title()}!")
            
greet_user()



