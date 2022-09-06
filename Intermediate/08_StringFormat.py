# Str.formate  = optional method that gives users 
#                more control when displaying output

number = 10000

print ("The number pi is {:.3f}".format(number)) # display 3 digits after the dicimal portion
print ("The number is {:,}".format(number)) # format the digits by 3 
print ("The number is {:b}".format(number)) # displaying the value in binary 
print ("The number is {:o}".format(number)) # displaying the value in octal 
print ("The number is {:X}".format(number)) # displaying hexadecimal 
print ("The number is {:x}".format(number)) # displaying hexadecimal lowercase
print ("The number is {:E}".format(number)) # displaing the value in scientific view
print ("The number is {:e}".format(number)) # displaing the value in scientific view in lowercase


animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)
print("THe {} jumped over the {}".format("cow","moon"))
print("THe {} jumped over the {}".format(animal, item))
print("THe {1} jumped over the {0}".format(animal, item)) # positional argument
print("THe {animal} jumped over the {item}".format(animal="Cat", item = "dog")) # positional argument


text = "The {} jumped over the {}"
print (text.format(animal, item))

name = "Bro"
print("Hello , my nameis {}".format(name))
print("Hello , my nameis {:10}. Nice to meet you".format(name)) # adding 10 char space after the formatter.
print("Hello , my nameis {:<10}. Nice to meet you".format(name)) # adding 10 char space after the formatter.
print("Hello , my nameis {:>10}. Nice to meet you".format(name)) # adding 10 char space before the formatter.
print("Hello , my nameis {:^10}. Nice to meet you".format(name)) # adding 10 char space center the formatter.
#print("Hello , my nameis {index:10}. Nice to meet you".format(name)) # adding 10 char space after the formatter.
#print("Hello , my nameis {variableName:10}. Nice to meet you".format(name)) # adding 10 char space after the formatter.

