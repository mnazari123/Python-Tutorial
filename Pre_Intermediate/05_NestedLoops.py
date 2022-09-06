# Nested Loops = the "inner loop" will finish all its interaction before
#                finishing one iteration of the "outer loop"

from symtable import Symbol


rows = int(input("How many rows? : "))
columns = int(input("How many columns? : "))

symbol = input("Enter a symbol to use")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()


