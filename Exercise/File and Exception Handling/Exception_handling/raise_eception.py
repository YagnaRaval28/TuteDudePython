age=int(input("Enter your age:"))
if age<0:
    raise ValueError("Age cannot be negative")
elif age>=18:
    print("You can vote")
else:
    print("You have to wait for some years to vote")    