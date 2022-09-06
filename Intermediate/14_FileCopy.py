# CopyFile() = copies contents of a file
# copy()     = copyfile() + permission mode + distination can be a directory
# copy2()    = copy() + copies metadata (file's creation and modification times)

import shutil

source = "/home/bibok/Documents/GitHub/Python-Tutorial/Intermediate/test.txt"
distination = "/home/bibok/Documents/GitHub/Python-Tutorial/Intermediate/copy.txt"
shutil.copyfile(source, distination) # source, distination
