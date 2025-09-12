"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
task1_float= 8.90
task1_int= int(task1_float)
print(task1_float)
print(task1_int)
#I labled both varibles and typed out a float then asked python to change the float to an interger using the function "int".
"""
TASK 2:
Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
postiveor= float(input("number:"))
if postiveor > 0: print("ok now you know the number is postive")
elif postiveor < 0: print("yea the number is negitve")
else: print("the number is zero")
# I decided to use a float for the number input then righting the if statment syaing if gretaer than 0 then it is postive and if less then 0 it is negative and no number will equal its base value 0.
"""
TASK 3:
Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
maththingy1=float(input("First Float Number-->"))
maththingy=int(input("Secound Interger Number-->"))
maththingyadd= maththingy1 + maththingy
maththingysubtract= maththingy1 - maththingy
maththingydivide= maththingy1 / maththingy
maththigymultiple= maththingy1 * maththingy
print(f"+ Equals {maththingyadd}")
print(f"- Equals {maththingysubtract}")
print(f"/ Equals {maththingydivide}")
print(f"* Equals {maththigymultiple}")
# I started off righting inputs for both interger and float then writing out new varibles for the the math of my intergers using the respective symbols then printing them out using the "f" function to my varibles to print out the words that are in that siad vairible. 
"""
TASK 4:

Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
JadenGsfruit_Basket = {
    "Butter-Butter No Mi": 1,
    "Chop-Chop No Mi": 1,
    "Grapefurit": 7
}
print("I have", JadenGsfruit_Basket["Grapefurit"],"Grapefruit")
print("I Have", JadenGsfruit_Basket["Chop-Chop No Mi"],"Chop-Chop No Mi")
#
"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""
tango_line = "420,67,456"
tango_rangled = tango_line.split(",")
tango_string = tuple(int(num) for num in tango_rangled)
print("String One", tango_line)
print("Tuble One",tango_rangled)
"""
TASK 6:

Create a list of your favorite subjects (as strings). 
Use the join() function to combine all subjects into a single string separated by commas.
Then create another version using " - " as the separator.
Print both the original list and both joined strings.
"""
pokemans =["Kangaskhan","Pidgeot,","Pinsir","Gengar","Mr.Mime","Kabutops"]
poekmans_team = ",".join(pokemans)
pokemans_team = "-".join(pokemans)