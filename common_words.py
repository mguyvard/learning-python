
filename = ['alice.txt', 'siddhartha.txt.', 'moby_dick.txt', 'little_women.txt']

for file in filename:
    try:
        with open(file, encoding='utf-8') as f:
            content = f.read()        
    except FileNotFoundError:
        pass
    else:
        number_of_occurence = content.lower().count(' the ')
        print(f"In the file {file}, the word 'the ' appears {number_of_occurence}")  

