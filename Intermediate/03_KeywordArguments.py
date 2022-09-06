# Keyword Arguments = arguments proceded by an identifier when we pass them to a fuction 
#                     the order of the argument does not matter, unlike positional arguments 
#                     Python knows the name of the argument that our function receives

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello(last="Code", first="Bro", middle="Dude")