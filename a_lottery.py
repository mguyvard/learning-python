from random import randint, choice 

class Die:
    def __init__(self, sides = 6):
        self.sides = sides
        
    def roll_die(self):
        showing_face = randint(1, self.sides)
        print(f"Rolling result: {showing_face}")
        
my_die = Die(10)

for i in range(1, 11):
    my_die.roll_die()  
    
print("/------------------------------------------/")

# my_list = ["g", 10, 34, 23, "a", 78, "w", 12, 1, "c", 9, 0, 29, 100, "e"]

i = 1
while i <= 5:
    success = 0
    trials = len(range(1, 3_000_000))
    for value in range(1, 101):   
        if choice(my_list) == "e":
            success += 1
    print(f"{success/trials}-% chance of winning")
    i += 1        

