# Tuple = Collection which is ordered and unchangeable
#         used to group together related data


student = ("Bro", 21, "male")

print(student.count("Bro")) # prints number of times an item exist

print(student.index("male")) #prints the index of an item position in the tuple


for x in student: # reading the tuple like a list
    print(x , end=" ") 

if "Bro" in student: # checking if an item is existed in a tuple
    print("Bro is here")