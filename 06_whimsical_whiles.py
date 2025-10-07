"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""
z = 0
while z < 10:
    z += 1
    print(z)
# I made a input told the user I wanted zero and I worte how much I want it to go up by in the body loping it till it reaches 10 its highest value.
"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""
print()
print()
print()

q = 11
while q > 1:
  q -= 1
  print(q)
# I frist labled the whole number then wrote a while function that says if my varible is greater than one subtract one.
"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""
facint = int(input("Enter Whole Number: "))
one = 1
while facint > 1:
   one = facint * one 
   facint -= 1
   print(facint)
   # I frist made a user input for the user to input a whole number then did the math for it to desend or add.
"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""
passs = "dojyaaan"
tryit = input("Test your might (enter password): ")
print()
while tryit != passs:
   print("You not gonna get it")
   tryit = input("Test your might (enter password): ")
   print("you got the jojo refrence welcome.")

   # made a user input then I wrote a while statement that repeats the input if the password is incorrect.
"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
enter = int(input("Enter a number: "))
summ = 0
while enter > 0:
   digi = enter % 10
   summ = summ + digi
   enter = enter // 10
   print("The sum is", summ)
   # I started by adding a user input then writing my while function with the match equation i wanted to use.
"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""
new = int(int("Enter a Number: "))

z, a = 0,1
coun = 0

while coun < new:
   print(z)
   z, a = z, a + z
   coun += 1
   # wrote out how i want the squence to be read to countinue the number count.