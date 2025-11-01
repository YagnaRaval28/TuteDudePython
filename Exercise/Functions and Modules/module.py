"""
.py file is a module
built-in modules
math,random,datetime

To import module 
Syntax- import module_name
To import only few functions/methods from module 
Syntax-from module_name import method_name
"""

import math
num=100
print(math.sqrt(num))

# Calculate area of a circle
radius=5
area=math.pi*(radius**2)
print(area)

#Syntax for creat an alias of the module that is imported:- import module_name as alias_name

import datetime as dt
t=dt.time(8,45,40)
print(t)