contact = {}

while True:
    print("Contact Book")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Show Contact")
    print("4. Quit")
    Userchoice = input("Input Number 1-4: ")

    if Userchoice == "1":
        personame = input("Enter Name: ")

        theyphone = input("Enter 10-digit phone number: ")
        if theyphone.isdigit() and len(theyphone) == 10:
            contact[personame] = theyphone
            print("Contact added")

        else:
            print("Phone number must be 10 digits")
    elif Userchoice == "2":

        personame = input("Enter Name to Remove: ")
        if personame in contact:
            del contact[personame]
            print("Contact Removed")

        else:
            print("Contact not in list.")

    elif Userchoice == "3":
        if contact:
            print("Contact list.")
            for personname in contact:
                print(personname + ": " + contact[personame])
            else:
                print("Person not found.")
        elif Userchoice == "4":
            print("See you soon")
            break
# I frist started by making a dictonary to store the entered contacts in next I started writing the if statments for every number input that the user wants to do then for number 4 quit i used break to end the while loop.




