"""
num=1
while num<5:
    print(num)
    num+=1
"""    
correct_password="Python"
while True:
    curr_password=input("Enter your password:")
    if curr_password==correct_password:
        print("Your password is correct! Congrats")
        break #no break statement can lead us to infinite loop
    else:
        print("Wrong Password!. Try again")
print("out of the loop")    