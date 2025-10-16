"""
Task 1: Greeting
Write a function that takes a name as a 
agrument and prints a greeting message like "Hello, [name]!".
"""
def greeting(name):
    """This function takes a name of your choice and prints a message greeting the name"""
    print("Hello, " + name + "!")
greeting("Donii_Boii")
"""
Task 2: Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""
def squarenum(numb):
    """This def function takes a intinger and multiplys them."""
    return numb * numb
"""
Task 3: Even or Odd
Write a function that takes a number as a argument that 
returns `True` if the number is even, and `False` otherwise.
"""
def even(numbe):
    """This def function will check if the number is true or flase by seeing if the number is even or odd"""
    return numbe % 2 == 0
"""
Task 4: Area of a Rectangle
Write a function that takes the length and width of a rectangle and returns its area.
"""
def find_area(length, width):
    """This def funcition will take two intengers and multiply them to find the area of a rectangle"""
    return length * width

"""
Task 5: Celsius to Fahrenheit
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""
def convert(seltzer):
    """This def function will convert the users input of celesicus and convert it to frienhiet"""
    return  (seltzer * 9/5) + 32
"""
Task 6: Average of Numbers
Write a function that takes a list of numbers as an argument
and returns the average (mean) of those numbers.
"""
def aveg(numr):
    """This def function will find the arverage in the list of numbers"""
    return sum(numr) / len(numr)
"""
Task 7: Total Calculator
Create a function that has arguments for the price and quantity of something, 
and returns the total.
"""
def summ(price, quanity, discount=0.0):
    """This def function will tell you the price of an item and the qauninty and then adding discount if you have one."""
    subsumm = price * quanity
    if discount > 0:
        subsumm = subsumm - (subsumm * discount)
        return subsumm
"""
Your function should also optionally accept a 3rd argument for discount as a float, 
and return the discounted if provided.
"""