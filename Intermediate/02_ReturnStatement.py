# return statement = Functions send python values/objects back to the caller.
#                    These values/objects are known as the function's return type


def multiply(x, y):
    #return x * y
    result = x * y
    return result

z = multiply (6, 8)

print(z)