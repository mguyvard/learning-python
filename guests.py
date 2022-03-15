filename = 'guest_book.txt'
answer = True
while answer:
    name = input("Hello, what is your name (q to quit): ")
    if name != "q":
        print(f"Hello {name.title()}")
        with open(filename, 'a') as client_name:
            client_name.write(f"{name.title()} visited us a while ago!\n")
    else:
        answer = False
        print("Bye-bye!")
              
