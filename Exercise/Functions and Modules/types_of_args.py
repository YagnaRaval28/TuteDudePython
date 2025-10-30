def sum(num1,num2):
    return num1+num2

# Positional arguments- Passing the arguments in order of their position
result=sum(15,20)

# Default arguments
result=sum(15,num2=20)

# The non-default arguments should not follow the default arguments


# Keyword-arguments
def add(a,b=5,c=10):
    return a+b+c
print(add(15,c=50)) #15+5+50=70