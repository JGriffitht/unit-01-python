enter_numeber1 = int(input("Input Number: "))
enter_numeber2 = int(input("Input Number: "))
# First off made my float inputs
print("Select Operation")


print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponents")
print("6. Floor Division")
print("7. Remainder")

whatisit = input("Enter Choice here: ")
#I made a text showing all the operations and made a slection choice by givin the user an input.
mathadd = enter_numeber1 + enter_numeber2
mathsubtract = enter_numeber1 - enter_numeber2
mathmulti = enter_numeber1 * enter_numeber2
mathdiv = enter_numeber1 / enter_numeber2
mathfloordiv = enter_numeber1 // enter_numeber2
mathexpo = enter_numeber1 ** enter_numeber2
mathremainder = enter_numeber1 % enter_numeber2
# Next I wrote down all my operations and varibles.
if whatisit == "1":
    print(f"Result of Add = {mathadd}")
if whatisit == "2":
    print(f"Result of Subtract = {mathsubtract}")
if whatisit == "3":
    print(f"Result of Multi = {mathmulti}")
if whatisit == "4":
    print(f"Result of div = {mathdiv}")
if whatisit == "5":
    print(f"Result of floor div = {mathfloordiv}")
if whatisit == "6":
    print(f"Result of expo = {mathexpo}")
if whatisit == "7":
    print(f"Result of Remainder = {mathremainder}")
#Lastly I Made all the if statments for what will be chosen and used the f funtion to take the th pervious varibles and use it in the users choice