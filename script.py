x = 1
y = 2

#print(x + y)
#print(x)

def add_numbers(x, y, z=None):
    if (z == None):
        return x + y
    else:
        return x + y + z
    return x + y + z

#print(add_numbers(1, 2))
#print(add_numbers(1, 2, 3))

def do_math(a, b, kind='add'):
    if (kind == 'add'):
        return a + b
    else:
        return a - b

#print(do_math(1, 2))

x = (1, 'a', 2, 'b')
#print(type(x))

x = [1, 'a', 2, 'b']
#print(type(x))

x.append(3.3)
#print(x)

"""
for item in x:
    print(item)
"""
    
i = 0
while (i != len(x) ):
    print(x[i])
    i += 1
    