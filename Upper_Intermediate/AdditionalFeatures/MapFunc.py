# map() = applies a fucntion to each item in an iterable (list, tuple, etc)
#
# map(function, iterable)

store = [("shirt", 20.00),
        ("pants", 25.00),
        ("Jacket", 50.00),
        ("Socks", 10.00)]

to_euros = lambda data : (data[0], data[1]*0.82)
to_dollars = lambda data : (data[0], data[1]/0.82) # coverting to US dollars

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)

