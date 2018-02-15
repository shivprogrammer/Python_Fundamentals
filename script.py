x = 1
y = 2

#print(x + y) // return 3
#print(x) // return 1

def add_numbers(x, y, z=None):
    if (z == None):
        return x + y
    else:
        return x + y + z
    return x + y + z

#print(add_numbers(1, 2)) // return 3
#print(add_numbers(1, 2, 3)) // return 6

def do_math(a, b, kind='add'):
    if (kind == 'add'):
        return a + b
    else:
        return a - b

#print(do_math(1, 2)) // return 3

x = (1, 'a', 2, 'b')
#print(type(x)) // return tuple

x = [1, 'a', 2, 'b']
#print(type(x)) // return list

x.append(3.3)
#print(x) // return [1, 'a', 2, 'b', 3.3]

#for item in x:
#    print(item)
    
#i = 0
#while (i != len(x) ):
#    print(x[i])
#    i += 1
 
# BOTH OF THE PREVIOUS LOOPS RETURN THE SAME RESULT
   
print([1, 2] + [3, 4])
print([1] * 3)
print(1 in [1, 2, 3])