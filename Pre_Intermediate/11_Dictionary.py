# Dictionay  = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing; allow us to access a value quickly


capital = {'US': 'Washington DC',
            'India': 'New Dehli',
            'Russia': 'Moscow',
            'China': 'Beijing'
            }

print(capital['Russia'])
# print(capital['Germany']) // returns error because it does not exit
# so we use the get method to check if it exist. 

print(capital.get('Germany'))
print(capital.keys())
print(capital.values())
print(capital.items()) # entire the dictionary including key and value

print()
capital.update({'Germany':'Berlin'})
capital.updata({'US':'Los Vegas'})

capital.pop('China') #remove the item
capital.clear() # remove all the items.  

for key,value in capital.items():
    print(key, value)