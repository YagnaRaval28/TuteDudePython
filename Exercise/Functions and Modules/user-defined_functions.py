"""
def greetings(name):
    print(f"Hellow {name}")
    print("Good Morning how are you?")

# Calling greetings function    
greetings("Yagna")    
"""

"""
def odd_or_even(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
num=int(input("Enter number:"))
odd_or_even(num)
"""

def sum(num1,num2):
    return num1+num2,num1-num2,num1*num2
val1,val2,val3=sum(10,5)
print("Sum:",val1,"\nSub:",val2,"\nMul:",val3)