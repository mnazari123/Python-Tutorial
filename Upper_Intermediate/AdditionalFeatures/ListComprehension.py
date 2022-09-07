# List Comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda fucntion, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditioal]
#                       list = [exprssion if/else for item in iterable]


squares = []                # create an empty list
for i in range (1, 11):     # create a for loop
    squares.append(i*i)     # define what each loop iteration should be
print(squares)

#List Comprehension
squares = [ i * i for i in range(1, 11)]
print(squares)


students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
passed_students = list(filter(lambda data : data >= 60, students))

print(passed_students)

#List Comprehension
passed_students = [i for i in students if i >= 60]
print(passed_students)
passed_students = [i if i >= 60 else "Failed" for i in students]
print(passed_students)
