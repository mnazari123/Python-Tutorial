import os


import os

path = "/home/bibok/Documents/GitHub/Python-Tutorial/Intermediate/test.txt"

if os.path.exists(path):
    print("That location exist")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path) : 
        print("That is a directory")
else : 
    print("That location does not exist")
