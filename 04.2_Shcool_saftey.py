How_Many_Line = int(input("How Many Are In Line: "))
How_Many_Minutes = int(input("How Much Minutes: "))
What_Grade_In = int(input("What Grade are you in 6th - 12th: "))
Have_Money = input("Do you Have money (yes or No)").strip().lower()
On_FreeFree = input("Are you on the free lunch list (yes Or No)").strip().lower()
# I first started writing My Varibles for what is happing in the prompt.
MoneyFood = Have_Money == "yes" or On_FreeFree == "yes"
Timme = True
if How_Many_Line > 25:
   Timme = How_Many_Minutes > 15
Piroirty = False
if How_Many_Line > 30 and What_Grade_In in [6, 7, 8]:
   Piroirty = True
if MoneyFood and Timme:
 print("Go Get Lunch")
 if Piroirty:
  print("Skip Line and Get Lunch due to Grade")
else:
  print("No Lunch Sorry")
  # I wrote the the varibles into the if statments and use booleans to remmber if the inputed grade,time and line number is going to get the student lunch or not.

