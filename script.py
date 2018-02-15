x = 1
y = 2

#print(x + y) // 3
#print(x) // 1

def add_numbers(x, y, z=None):
    if (z == None):
        return x + y
    else:
        return x + y + z
    return x + y + z

#print(add_numbers(1, 2)) // 3
#print(add_numbers(1, 2, 3)) // 6

def do_math(a, b, kind='add'):
    if (kind == 'add'):
        return a + b
    else:
        return a - b

#print(do_math(1, 2)) // 3

x = (1, 'a', 2, 'b')
#print(type(x)) // tuple

x = [1, 'a', 2, 'b']
#print(type(x)) // list

x.append(3.3)
#print(x) // return [1, 'a', 2, 'b', 3.3]

#for item in x:
#    print(item)
    
#i = 0
#while (i != len(x) ):
#    print(x[i])
#    i += 1
 
# BOTH OF THE PREVIOUS LOOPS RETURN THE SAME RESULT
   
#print([1, 2] + [3, 4]) // [1, 2, 3, 4]
#print([1] * 3) // [1, 1, 1]
#print(1 in [1, 2, 3]) // True

x = 'This is a string'
#print(x[0]) // 'T'
#print(x[0:1]) // 'T'
#print(x[0:2]) // 'Th'
#print(x[-1]) // 'g'
#print(x[-4:-2]) // 'ri'
#print(x[:3]) // 'Thi'
#print(x[3:]) // 's is a string'

x = 'Dr. Christopher Brooks'
#print(x[4:15]) // 'Christopher'

firstname = 'Christopher'
lastname = 'Brooks'
#print(firstname + ' ' + lastname) // 'Christopher Brooks'
#print(firstname * 3) // 'ChristopherChristopherChristopher'
#print('Chris' in firstname) // True

firstname = 'Christopher Arther Hansen Brooks'.split(' ')[0]
lastname = 'Christopher Arthur Hansen Brooks'.split(' ')[-1]
#print(firstname) // 'Christopher'
#print(lastname) // 'Brooks'