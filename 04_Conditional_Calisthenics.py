'''
Exercise 1:
Check if an integer is greater than 10.
Return True if conditions are met, False otherwise.
'''
Lets_check = int(input("Place Your Number here."))
if Lets_check > 10:
    print("This True")
else:
    print("This Flase")
    # I Made a Varible for user input then made a if else statment finding out if the user input is greater than 10 or less than.
'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''
Age_Entry = int(input("Enter Your Age"))
if Age_Entry == 18:
    print("The price is 20$ for entry")
else:
    print("The Price is 10$ for entry")
# I made a interger input for age then writing an if statment telling it what to print for each age.
'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''
From_JadenGs_FruitBasket = (input("Enter A fruit from my fruit basket")).strip().upper()
JadenGsfruit_Basket = ["butter-butter no mi","chop-chop No mi","grapefruit"]
print(JadenGsfruit_Basket)
if From_JadenGs_FruitBasket in From_JadenGs_FruitBasket:
    print("Yes This fruit is in the basket.")
else:
    print("No this fruit is not here in my basket.")

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''
How_Heavy = float(input("Enter the order weight in kg: "))
Where_is_it = input("Enter the destination zone (Z or E): ").strip().upper()
if How_Heavy < 0:
    print("Weight less than 0 kg")
else:
    if Where_is_it == "Z":
        cost = How_Heavy * 5
        print(f"Shipping to Zone Z: ${cost:.2f}")
    elif Where_is_it == "E":
        cost = How_Heavy * 7
        print(f"Shipping to Zone E: ${cost:.2f}")
    else:
        print(" Not a Zone Invalid zone")
'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''