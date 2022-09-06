#List = used to store multiple items in a single variable

food = ["Pizza", "Humberger", "Hotdog", "Spaggetti", "Pudding"]

print (food) # print the list in a list style 
print(food[1]) # printing an item at a special index

food[0] = "Sushi" # replacing an item in the list according to its index
print(food)
food.append("Ice-cream") # adding an item at the end of the list
print(food)
food.remove("Hotdog") # removing an item based on its name
print(food)
food.pop() # removing an item from the end of the list
print(food)
food.insert(0, "Cake") # insert an item at specific position in the list
print(food)
food.sort() # sort a list alphabitically 
print(food)
food.clear() # remove all of the elements in a list

#for f in food:
    #print(f)

