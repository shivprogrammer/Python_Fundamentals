# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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

print(add_numbers(1, 2))
print(add_numbers(1, 2, 3))