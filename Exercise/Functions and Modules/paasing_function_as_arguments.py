# In python, we can pass function as arguments of another function

def add1(num):
    return num+1

def square(num):
    return num**2

num=int(input("Enter int:"))
res_1=add1(num)
res2=square(res_1)
#res=square(add_1(num))
print("Output:",res2)

