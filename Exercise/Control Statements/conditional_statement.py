# ==,>=,<=,!=,>,<
"""
age=float(input("Enter your age:"))
if age>=18:
    print("Congrats!. You are an adult. You can vote")
else:
    print("After few years you can vote!!!")  

"""      

"""
num=int(input("Enter number:"))
if num==0:
    print("Number is zero")
elif num%2==0:
    print("Number is even")
else:
    print("Number is odd")        

"""

#Nested if
num=int(input("Enter marks:"))
if num>60:
    print("You have passed")
    if num>=90:
        print("You got A grade")
    elif num<=89 and num>80:
        print("You got B grade")
    else:
        print("You got C grade")        
else:
    print("You Failed")    
