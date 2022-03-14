file_path = '/home/guyvard/pi_dig_folder1/pi_dig_folder2/pi_147048_digits.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines: 
    pi_string += line.strip()
    
birthday = input("Enter your birthday in the form ddmmyyyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first 147048 of pi!")
else:
    print("Your birthday doesn't appear in the first 147048 of pi!")
    
