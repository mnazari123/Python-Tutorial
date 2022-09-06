
path = "/home/bibok/Documents/GitHub/Python-Tutorial/Intermediate/test.txt"

try: 
    with open (path) as file: # with opens and closes the file connection
        print(file.read())
except FileNotFoundError: 
    print("That file was not found: ")