import os

source = "/home/bibok/Documents/GitHub/Python-Tutorial/test.txt"
distination = "/home/bibok/Documents/GitHub/Python-Tutorial/Intermediate/test.txt"

try: 
    if os.path.exists(distination):
        print("There is already a file existed")
    else:
        os.replace(source, distination)
        
        print(source + " was moved")
except FileNotFoundError:
    print(source + " The file was not found")