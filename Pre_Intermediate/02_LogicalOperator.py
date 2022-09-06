#Logical Operator (and, or, not) = used to check if two or more conditional statements are true

temp = int(input("What is the temprture outside? "))

if not(temp >= 0 and temp <= 30):
    print("The temprature is bad today")
    print("stay inside")
elif not(temp < 0 or temp > 30):
    print("The temprature is good today")
    print("go outside")




