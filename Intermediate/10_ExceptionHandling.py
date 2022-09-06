# Exception = events detected during execution that interrupt the flow of a program

try: 
    numerator = int(input("Enter a number to divide: "))
    denomenator = int(input("Enter a number to divide by: "))
    result = numerator / denomenator
except ZeroDivisionError as e:
    print (e)
    print("You can not divid by zero")
except ValueError as e:
    print(e)
    print("Enter only numbers please")
except Exception as e:
    print (e)
    print("Something went wrong : (")
else: # it print only if there is no excpetion.
    print ("The result is : " + int(result))
finally: # it is mostly used when we are closing a file or something to be done at the end
         # File Handling
    print("This will always execute")