#Lambda Function = Function written in 1 line using lambda keyword
#                  accepts any number of argument, but only has one expression
#                  (think of it as a shortcut)
#                  (useful if needed for a short period of time, throw-away)

# lambda parameters : expression 

def double(x):
    return x*2

print(double(5))

doubling = lambda x : x * 2
print(doubling(5))
multiplying = lambda x, y : x*y
print(multiplying(5, 5))

add = lambda x, y , z : x+y+z;
print(add(10, 20, 30))

fullname = lambda firstname, lastname : firstname + " " + lastname
print(fullname("Bro", "Code"))

age = lambda age : True if age>= 18 else False
print(age(20))
