#Set = Collection which is unordered, unindixed. No duplicate values

from curses import update_lines_cols

utensils = {"fork", "spoon", "knife"}

for u in utensils: 
    print(u)

dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkine")
utensils.remove("fork")
utensils.clear()
dishes.update(utensils)

dinner_table= utensils.union(dishes)

print(dishes.difference(utensils))
print(utensils.intersection(dishes)) # in common

for x in dinner_table: 
    print(x)