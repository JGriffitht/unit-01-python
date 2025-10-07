
todo_tracker = []

while True:
    print("Your TODO's are: ")
    indent = 0
    while indent < len(todo_tracker):
        print(str(indent + 1)+")"+todo_tracker[indent])
        indent = indent + 1
        print("Update List")
        print()
        print("Add")
        print()
        print("Remove")
        print()
        print("(Quit) -To Stop-")
        print()
        print()
        what_the_user_wants = input("What do you want to do: ").strip().lower()
# Made a while statment to keep reprinting the list and the quesitons of wnat the user wants to do.
        if what_the_user_wants == "add":
            adding = input("Add to your list: ")
            todo_tracker.append(adding)
            print()
            print()
        elif what_the_user_wants == "remove":
            removenum = int(input("Enter the number task you want to remove: "))
            if removenum >= 1 and removenum <= len(todo_tracker):
                removing = todo_tracker[:removenum -1]
                removed = todo_tracker[removenum: ]
                todo_tracker = removing + removed
                print( )
        