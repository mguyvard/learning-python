filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as filename1:
            contents= filename1.read()
        print(contents, "\n")
    except FileNotFoundError:
        pass
        
