# Loop Control Statement = change a loop execution from its normal sequence

# break = used to terminate the loop entirely 
# continue = used to skip to the next iteration of the loop
# pass = does nothing; acts as a placeholder 

while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number : 
    if(i == "-"):
        continue
    print(i, end="")
print()
for i in range(1, 10):
    if (i % 2 == 0):
        pass
    else:
        print(i , end=" ")
 



