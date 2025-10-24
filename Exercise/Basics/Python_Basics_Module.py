"""#Area and Perimeter of Triaangle
a=int(input("Enter Side 1:"))
b=int(input("Enter Side 2:"))
c=int(input("Enter Side 3:"))
p=(a+b+c)/2
area=(p*(p-a)*(p-b)*(p-c))**0.5
print("Perimeter:",p)
print("Area:",area)"""

#Simple interest
p=float(input("Enter Principle:"))
r=float(input("Enter rate of interest:"))
n=float(input("Enter number of years:"))
simple_interest=(p*r*n)/100
print("Simple Interest:",simple_interest)