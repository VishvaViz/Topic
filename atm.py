print("******** WELCOME TO THE ATM ******")

print("**Please Insert your ATM Card***")

pin=int(input("Enter the Pin Number:"))
bal1=10000
bal2=20000
bal3=30000
bal4=40000

pin1=9585
pin2=1234
pin3=2222
pin4=3333

if pin==pin1:
    print("1 Witdraw")
    print("2 Cash Depoist")
    print("3 Balance Enquiry")
    print("4 Fast Cash")
    choose=int(input("Select the Trantactions you want:"))
    
    if choose==1:
        print("1 Savings Account")
        print("2 Current Account")
        acc_type=str(input("Selcet the Account Type "))
        if acc_type==1 or 2:
            witdraw=int(input("Enter the Amount:"))
        if witdraw<=bal1:
            print(f"Please Collect Your Cash:{witdraw}")
            balance_amt=bal1-witdraw
            print(f"Your Account Balacne is:{balance_amt}")
        else:
            print("Insufficent Balance")
    elif choose==2:
        deposit_amt=int(input("Enter the Amount To be Deposited:"))
        deposit_amt=deposit_amt+bal1
        if deposit_amt==deposit_amt:
            print(f"Your Amount is Deposited Account Balance Is:{deposit_amt}")
        else:
            print("Error")
    elif choose==3:
        print(f"Your Account Balance is:{bal1}")
    elif choose==4:
        print("witdraw Rs:3000")
        print("witdraw Rs:5000")
        print("widraw Rs:7000")
        select_amt=int(input("Select the Which You want:"))
        if select_amt==3000 and bal1:
            print(f"Please Collect Your Cash:{select_amt}")
            bal_amt=bal1-select_amt
            print(f"Your Account Balance is:{bal_amt}")
        elif select_amt==5000 and bal1:
            print(f"Please Collect Your Cash{select_amt}")
            bal_amt=bal1-select_amt
            print(f"Your Account Balance is:{bal_amt}")
        elif select_amt==7000 and bal1:
            print(f"Please Collect Your Cash:{select_amt}")
            bal_amt=bal1-select_amt
            print(f"Your Account Balance:{bal_amt}")

if pin==pin2:
    print("1 Witdraw")
    print("2 Cash Depoist")
    print("3 Balance Enquiry")
    print("4 Fast Cash")
    choose=int(input("Select the Trantactions you want:"))
    
    if choose==1:
        print("1 Savings Account")
        print("2 Current Account")
        witdraw=int(input("Enter the Amount:"))
        if witdraw<=bal2:
            print(f"Please Collect Your Cash:{witdraw}")
            balance_amt=bal2-witdraw
            print(f"Your Account Balacne is:{balance_amt}")
        else:
            print("Insufficent Balance")
    elif choose==2:
        deposit_amt=int(input("Enter the Amount To be Deposited:"))
        deposit_amt=deposit_amt+bal2
        if deposit_amt==deposit_amt:
            print(f"Your Amount is Deposited Account Balance Is:{deposit_amt}")
        else:
            print("Error")
    elif choose==3:
        print(f"Your Account Balance is:{bal2}")

    elif choose==4:
        print("witdraw Rs:3000")
        print("witdraw Rs:5000")
        print("widraw Rs:7000")
        select_amt=int(input("Select the Which You want:"))
        if select_amt==3000 and bal2:
            print(f"Please Collect Your Cash:{select_amt}")
            bal_amt=bal2-select_amt
            print(f"Your Account Balance is:{bal_amt}")
        elif select_amt==5000 and bal2:
            print(f"Please Collect Your Cash{select_amt}")
            bal_amt=bal2-select_amt
            print(f"Your Account Balance is:{bal_amt}")
        elif select_amt==7000 and bal2:
            print(f"Please Collect Your Cash:{select_amt}")
            bal_amt=bal2-select_amt
            print(f"Your Account Balance:{bal_amt}")

    
if pin==pin3:
    print("1 Witdraw")
    print("2 Cash Depoist")
    print("3 Balance Enquiry")
    print("4 Fast Cash")
    choose=int(input("Select the Trantactions you want:"))
    
    if choose==1:
        print("1 Savings Account")
        print("2 Current Account")
        witdraw=int(input("Enter the Amount:"))
        if witdraw<=bal3:
            print(f"Please Collect Your Cash:{witdraw}")
            balance_amt=bal2-witdraw
            print(f"Your Account Balacne is:{balance_amt}")
        else:
            print("Insufficent Balance")
    
    elif choose==2:
        deposit_amt=int(input("Enter the Amount To be Deposited:"))
        deposit_amt=deposit_amt+bal3
        if deposit_amt==deposit_amt:
            print(f"Your Amount is Deposited Account Balance Is:{deposit_amt}")
        else:
            print("Error")
    
    elif choose==3:
        print(f"Your Account Balance is:{bal3}")

    elif choose==4:
        print("witdraw Rs:3000")
        print("witdraw Rs:5000")
        print("widraw Rs:7000")
        select_amt=int(input("Select the Which You want:"))
        if select_amt==3000 and bal3:
            print(f"Please Collect Your Cash:{select_amt}")
            bal_amt=bal3-select_amt
            print(f"Your Account Balance is:{bal_amt}")
        elif select_amt==5000 and bal3:
            print(f"Please Collect Your Cash{select_amt}")
            bal_amt=bal3-select_amt
            print(f"Your Account Balance is:{bal_amt}")
        elif select_amt==7000 and bal3:
            print(f"Please Collect Your Cash:{select_amt}")
            bal_amt=bal3-select_amt
            print(f"Your Account Balance:{bal_amt}")

if pin==pin4:
    print("1 Witdraw")
    print("2 Cash Depoist")
    print("3 Balance Enquiry")
    print("4 Fast Cash")
    choose=int(input("Select the Trantactions you want:"))
    
    if choose==1:
        print("1 Savings Account")
        print("2 Current Account")
        witdraw=int(input("Enter the Amount:"))
        if witdraw<=bal4:
            print(f"Please Collect Your Cash:{witdraw}")
            balance_amt=bal2-witdraw
            print(f"Your Account Balacne is:{balance_amt}")
        else:
            print("Insufficent Balance")
    
    elif choose==2:
        deposit_amt=int(input("Enter the Amount To be Deposited:"))
        deposit_amt=deposit_amt+bal4
        if deposit_amt==deposit_amt:
            print(f"Your Amount is Deposited Account Balance Is:{deposit_amt}")
        else:
            print("Error")
    
    elif choose==3:
        print(f"Your Account Balance is:{bal4}")

    elif choose==4:
        print("witdraw Rs:3000")
        print("witdraw Rs:5000")
        print("widraw Rs:7000")
        select_amt=int(input("Select the Which You want:"))
        if select_amt==3000 and bal4:
            print(f"Please Collect Your Cash:{select_amt}")
            bal_amt=bal4-select_amt
            print(f"Your Account Balance is:{bal_amt}")
        elif select_amt==5000 and bal4:
            print(f"Please Collect Your Cash{select_amt}")
            bal_amt=bal4-select_amt
            print(f"Your Account Balance is:{bal_amt}")
        elif select_amt==7000 and bal4:
            print(f"Please Collect Your Cash:{select_amt}")
            bal_amt=bal4-select_amt
            print(f"Your Account Balance:{bal_amt}")
else:
    print("****Invalid Pin Number****")











