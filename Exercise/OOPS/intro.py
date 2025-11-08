class MyClass:
    """
    In the docstring
    """
    pass

obj1=MyClass()
obj2=MyClass()

l1=[4,5,6]
print(type(l1))

print(type(obj1))

# Calling methods
#obj1.method()

# Doc Strings
help(MyClass)
print(MyClass.__doc__)