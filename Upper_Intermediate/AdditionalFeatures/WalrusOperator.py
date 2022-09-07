# Walrus Operator := 
# it is a new concept in python 3.8
#assignment expression aka walrus operator
# assign values to variable as part of a larger expression

happy  = True
print(happy)
print(happy:=True) #walrus

foods = list()
while True:
    food = input("what food do you like: ")
    if food == "quit":
        break
    foods.append(food)

# the same program with walrus

foods = list()
while food := input("What food do you like: ") != "quit":
    foods.append(food)
