def hello():
    print("Hello")

print(hello) # prints the address in the main memory
hi = hello
print(hi) # prints the same addrss as long as both are refering to same variable value

hi = hello
hello()
hi()

say = print
say("Whoa! I can not believe it works :o")