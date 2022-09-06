import os
import shutil

source = "/home/bibok/Documents/GitHub/Python-Tutorial/Intermediate/copy.txt"

try:
    os.remove(source) # delete a file
    #os.rmdir(path) # delete a file or empty folder
    #shutil.rmtree(path) # delete files and or folders
except FileNotFoundError: 
    print("The file is not found")
except PermissionError:
    print("You do not have the permission to delete this file")
except OSError: 
    print("That folder contains files")
else:
    print(source + " was removed")
