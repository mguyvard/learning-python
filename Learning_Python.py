file_path = '/home/guyvard/learning-python/learning_python.txt'

with open(file_path) as file_name:
    content = file_name.read()    
print(f"{content.strip()}\n")    
print("---------------------------------------")

with open(file_path) as file_name:
    for line in file_name:
        print(f"{line.rstrip()}")
print("\n----------------------------------------")

py_string = ''
with open(file_path) as file_name:
    lines = file_name.readlines()
for line in lines:
    print(line.rstrip())
    
