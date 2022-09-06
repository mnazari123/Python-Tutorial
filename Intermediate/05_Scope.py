# Scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped version of a variable can be created

name = "Bro" # Global Scope (available inside & outside function)

def display_name(): 
    lname = "Code"   # local scope () available only inside this function
    print(lname)
    print(name) # accessible throughout the inside a function
                # it is possible to have two variable with the same names
                # 

display_name()
print(name)
