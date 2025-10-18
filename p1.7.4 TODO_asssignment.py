todos_tracker = []
while True:
    print("Your current todos are:")
    if todos_tracker:
        for z in range(len(todos_tracker)):
            print(str(z+1) + ") " + todos_tracker[z])
    else:
        print("You got no todos yet")
    print("add, remove, or quit?")
    choice = input("Type add , remove or quit: ").lower()
    if choice == "add":
        new_todo = input("What is your new todo? ")
        todos_tracker.append(new_todo)
        print("Added:", new_todo)
    elif choice == "remove":
        if todos_tracker:
            num = int(input("todo would you like to remove? "))
            if 1 <= num <= len(todos_tracker):
                removed = todos_tracker.pop(num-1)
                print("Removed:", removed)
            else:
                print("Invalid number.")
        else:
            print("No todos to remove.")
    elif choice == "quit":
        print("You Quit:", todos_tracker)
        break
    else:
        print("Invalid choice. Try again.")
# I first started off mmaking a list for the while loop to store the varibles then next adding a user choice seleciton for add removeing or quiting then using append to add new things to the list and then using len to add it to the list showing numbers for the the user next for removing from the list I used .pop to remove it from the list through the users input then using break to end the loop.