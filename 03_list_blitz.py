"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""
Why_want_this_list = ["Greninja", "Salamence",'Blastoise','Mewtwo',"Pikachu","Metagross"]
print(Why_want_this_list)
# I created a varible from my list then listed words for my list then printing it.
"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""
Why_want_this_list.append("Dedenne")
print(Why_want_this_list)
#I used .append to to add a new word.
"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""
Why_want_this_list.remove("Blastoise")
print(Why_want_this_list)
# I told It I wanted to remove an item from my list using .remove taking it out of the list.
"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""
Why_want_this_list[5] = "Emolga"
print(Why_want_this_list)
#I told it I want my word to be put in on the list in the fifth spot.
"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""
Why_want_this_list.append("Binacle")
Why_want_this_list.append("Binaclee")
Why_want_this_list.append("Binacleee")
print(Why_want_this_list)
# Added three new words to the list using .append.
"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""
del Why_want_this_list [8]
print(Why_want_this_list)
# I used "del" to tell it I want the eigth listed item in the list deleted.
"""
Task 7: Slicing lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""
slice_and_dice = Why_want_this_list[:5]
print(slice_and_dice)
#Created a varible told it I want my list cut at the fifth listed item then printed it.
"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""
Okay_Maybe_Grade = ["By","The","Way","Its","Only","Six"]
Why_want_this_list.extend(Okay_Maybe_Grade)
print(Why_want_this_list)
#I made a new list and added the the .extend then printed out the ornginal list with the extended list.