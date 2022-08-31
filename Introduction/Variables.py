
#String 
first_name = "Bro"
last_name = "Code"
full_name = first_name + " " + last_name;

print (type(last_name)) # for knowing the type of a variable 

print ("Hello " + full_name)

# Interger
age = 21

# print ("Age " + age ) // it will not work to concatenate String with integers
                        # indeed we can try another way of converting the integer into String first
print ("Age " + str(age)) # cast the int into string
age += 1 # increment 
age -= 1 # decrement 
print ("New Age " + str(age))

#float 

height = 1.78
print (height)
print (type(height))
print ("Your height is " + str(height) + "m")

# boolean.

human = False;
print (human);
print(type(human))
print ("Are you a human " + str(human))
