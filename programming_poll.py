filename = '/home/guyvard/polling_folder/programming_poll.txt'
next_answer = True
while next_answer:
    answer = input("Why do you like programming? (type q to quit)__")
    if answer != "q":
        with open(filename, 'a') as file_name:
            file_name.write(answer)
            file_name.write("\n")
    else:
        print("Bye-bye")
        next_answer = False
