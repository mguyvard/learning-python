
def count_words(filename):
    """Count the number of words in a text file"""
    try:
        with open(file, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass 
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = ['alice.txt', 'siddhartha.txt.', 'moby_dick.txt', 'little_women.txt']

for file in filename:        
    count_words(file)    
  
