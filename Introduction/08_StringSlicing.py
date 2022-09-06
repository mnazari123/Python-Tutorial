#Slicing = create a subtracting by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]


name = "Bro code"

first_name = name[:3] #    [0:3]
last_name = name[4:] #     [4:end] 
funky_name = name[0:8:1] # print each letter in the string;
print(funky_name)
funky_name = name[0:8:2] # printing every other character. 
print(funky_name)
funky_name = name[::1] 
print(funky_name)

reversed_name = name[::-1]
print(reversed_name)

website = "http://google.com"

slice = slice(7, -4)
print(website[slice])
