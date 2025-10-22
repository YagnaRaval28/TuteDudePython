#Couting substring from a given String
#count()
s1="We are learning Python. Python is fun"
s2="Python"
print(s1.count(s2))

#Changing case of a string
# upper(),lower(), capitalize(), title()
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.capitalize())

#Starting and Ending of a string
print(s1.startswith("We are"))
print(s1.startswith("are"))
print(s2.endswith("n"))