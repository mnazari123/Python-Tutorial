from distutils.util import execute


#while loop = is a statement that will execute as long as it condition remains true

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name);
