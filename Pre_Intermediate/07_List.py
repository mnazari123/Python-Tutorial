#List = used to store multiple items in a single variable

food = ["Pizza", "Humberger", "Hotdog", "Spaggetti", "Pudding"]

print (food) # print the list in a list style 
print(food[1]) # printing an item at a special index

food[0] = "Sushi" # replacing an item in the list according to its index

food.append("Ice-cream") # adding an item at the end of the list
food.remove("Hotdog") # removing an item based on its name
food.pop() # removing an item from the end of the list
food.insert(0, "Cake") # insert an item at specific position in the list
food.sort() # sort a list alphatically 
food.clear() # remove all of the elements in a list

#for f in food:
    #print(f)

