"""
Recursion is the process in a which function call itself till a certain condition is not met
"""
#Without recursion
def factorial(num):
    fact=1
    while num>1:
        fact*=num
        num-=1
    return fact   

print(factorial(5))

# With recursion
def fact(num):
    if num==1:
        return 1
    else:
        factorial_res=num*fact(num-1)
        return factorial_res
print(fact(5))    