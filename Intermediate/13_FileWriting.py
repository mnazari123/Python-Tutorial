
path = "/home/bibok/Documents/GitHub/Python-Tutorial/Intermediate/test.txt"
text  = "\nWrite some more text on the file"

with open (path, 'a') as file: # default is 'r' = read; it can be 'w' = write, a = append
    file.write(text) 