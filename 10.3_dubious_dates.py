import datetime
"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""
today = datetime.datetime.today()
print("Today's Date")
print()
print(today)
#labled both my varible and the function.
"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""
todaytwo = datetime.datetime.today()
date = todaytwo.strftime("%m/%d/%Y")
print("-------------------")
print("Today's Date 2")
print()
print(date)
# i used "strftime" to format how i want the date printed
"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""