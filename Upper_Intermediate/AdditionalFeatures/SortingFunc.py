#Sort() method = used with list not with tupples
#Sort() function = used with iterables

scholars = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
scholars.sort()
#scholars.sort(reverse=True) # in reverse order

Sorted_Studetns = sorted(scholars, reverse=True)
for i in scholars: 
    print(i)

students = [("Squidward", "F", 60), # list of tupples 
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)
            ]

grade = lambda grades:grades[1]
name = lambda name:name[0]
ages = lambda age:age[2]
students.sort(key=grade, reverse = True)
for i in students:
    print(i)

#sorted_students = sorted(students, key=ages, reverse=True)
sorted_students = sorted(students, key=ages)
for i in sorted_students:
    print(i)