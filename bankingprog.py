def Show_balance(balance):
    print("***************************************")
    print(f"   Your Balance is : ${balance:.2f}   ")
    print("***************************************")
def deposit():
    amount = float(input("Enter the amount to be deposited : "))
    if amount < 0:
        print("************************")
        print("    Invalid amount !    ")
        print("************************")
        return 0
    else:
        return amount

def withdraw(balance):
    amount  = float(input("Enter the amount to be withdrawn : "))
    if amount > balance:
        print("************************")
        print("  Insufficient funds !  ")
        print("************************")
        return 0
    elif amount < 0 :
        print("************************")
        print("    Invalid amount !    ")
        print("************************")
        return 0
    else:
        return amount
    

def main():
    balance = 0
    isrunning = True
    while isrunning:
        print("****************************")
        print("      Banking Program       ")
        print("****************************")
        print("  1.Balance")
        print("  2.Deposit")
        print("  3.Withdraw")
        print("  4.Exit")
        print("****************************")
        choice = input("Enter your choice (1-4) : ")
        match choice:
            case '1':
                Show_balance(balance)
            case '2':
                balance += deposit()
            case '3':
                balance -= withdraw(balance)
            case '4':
                isrunning = False
            case _:
                print("*********************")
                print("  Invalid Choice !   ")
                print("*********************")
    print("**************************************")
    print("    Thank You ! Have a nice day !     ")
    print("**************************************")
if __name__ == '__main__':
    main()