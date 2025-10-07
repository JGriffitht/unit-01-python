"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""
for t in range(1,11):
    print(t)
# made a for loop using ranges to cound all the numbers in the bracket.
"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""
for y in range(900,1001,10):
    print(y)
    #wrote out the the starting number then the ending number then told it how much to go up by
"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""
for u in range(1,101,9):
    print(u)
    #Wrote the 1 as its starting number 101 as its ending an 9 as its counting intervauls
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""
nanda = 0
for i in range(1,11):
    nanda += i
    print(nanda)
    # made a place holder for the total then wrote the for range loop.
"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?
The content of the code is *s.
- Explain the iterative process that this code executes to get that output
the proces it uses is using the number of rows it tells you in the varible row slot then adding the number of starts in that row that many times.
"""
rows = 5
 
for i in range(rows):
   for j in range(i + 1):
       print('*', end=' ')
   print()