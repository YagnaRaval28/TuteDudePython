def fact(num):
    factorial=1
    while num>1:
        factorial*=num
        num-=1
    return factorial
num=int(input("Enter a number:"))
print(f"Factorial of {num} is:{fact(num)}")