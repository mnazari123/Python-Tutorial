# *arg = parameter that will pack all argument into a tuple 
#        useful so that a function can accept a varying amount of argument 

def add(*stuff):
    sum = 0;
    print(stuff)
    stuff = list(stuff) # we convert it to list for bringing changes to argument
    stuff[0] = 0 # tuple objects are not changeable. for this we change them to list

    print (stuff)
    for i in stuff:
        sum += i
    return sum 

print (add(1,2, 3, 4, 5, 6))

def addition(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print (addition(1, 2, 4))