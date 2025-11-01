def check_balance():
    print("----------------------------------")
    print(f"You have {balance}$ in your account")
    print("----------------------------------")
def deposit():
    global balance
    amount=float(input("Enter amount you want to deposit:"))
    if amount<0:
        print("Invalid amount!!!")
        return
    balance+=amount
def withdraw():
    global balance
    amount=float(input("Enter amount you want to withdraw:"))
    if amount<0:
        print("Invalid amount!!")
        return
    if amount>balance:
        print("Not sufficient balance")
        return
    balance-=amount
balance=0    
if __name__=="__main__":
    print("----------------------------------")
    print("Welcome to Yagna_Raval PVT bank")
    print("----------------------------------")
    print("\n")
    while True:
        print("----------------------------------")
        print("1. Check balance of your account")
        print("2. Deposite an amount")
        print("3. Withdraw an amount")
        print("4. Quit")
        print("----------------------------------")
        choice=input("Enter your choice:")
        if choice=='1':
            check_balance()
        elif choice=='2':
            deposit()
        elif choice=='3':
            withdraw()
        elif choice=='4':
            
            break
        else:
            print("Invalid choice!!!, Retry")   
print("----------------------------------")                      
print("Thank you for banking with us")
print("----------------------------------")            