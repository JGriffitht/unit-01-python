Batchitem_ID = input("Enter Batch ID: ")
Batchinspector_ID = input("Enter Inspector ID: ")
production_day = input("What is the date: ")
# Frist I started off addding the varibles for my inputs that collects important data.
big_batch = int(input("Enter Nunmbers in batch: "))
# I set the batch size set stone to 50
passing = 0
Rejecting = 0
testing_catagories = {"none": 0,"minor": 0, "major": 0}
# I then added counters for the items and the item quality.
for l in range(1, big_batch + 1):
        print("ii", l)
        quilty = int(input("Enter Quality (1-10): "))
        defecterd = input("Enter the type of defect on prodect, (none,minor,major) :").lower()
# Made a range for the batch
if defecterd in testing_catagories:
        testing_catagories[defecterd] += 1
        if quilty >= 7 and defecterd == "none":
                passing += 1
        else: 
               Rejecting += 1
# Then I made my if statments testing for if the items are making it through or not.
print("Batch Id:", Batchitem_ID)
print("product day:", production_day)
print("Inspector id:", Batchinspector_ID)
print("pass:", passing)
print("reject:", Rejecting)
print("Defected:", testing_catagories)
#printed out the results.


