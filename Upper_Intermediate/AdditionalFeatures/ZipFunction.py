# zip (*iterable) = aggregate elements from two or more iterable (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element


usernames = ["Dude", "Bro", "mister"]
passwords = ["Password", "abc123", "guess"]

users = dict(zip(usernames, passwords))

print (type(users))

for key, value in users.items():
    print(key+ " : " + value)

loginDatas = ["1/1/2021", "1/2/2021", "1/3/2021"]
users = zip(usernames, passwords, loginDatas)
for i in users:
    print(i)
