# Function = a block of code which is executed only when it is called

def hello(first_name, last_name, age):
    print("hello " + first_name + " " + last_name)
    print("you are " + str(age) + " years old")
    print("Have a nice day")

hello("bro", "code", 21)

def perform():
    print("Show me this message")

perform()

first_name = "My Name"
last_name = "Lastname"
age = 33

hello(first_name, last_name, age)