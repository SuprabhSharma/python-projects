
print("\t\t\t\t\t\twelcome to the kotak atm")
amount = 100000
pin = 12345

if 'card' ==  input("enter your card number : "):
    print("welcome to kotak atm")
    if pin == int(input("enter valid pin: ")):
        print("\t\t\t\t\t1) WITHDRAWL \t\t\t\t\t 2) CHECK BALANCE")
        select = int(input("enter your option:"))
        if select==1:
            user_amount = int(input("enter the amount you want to withdrawl : ")) 
            amount = amount - user_amount
        elif select==2:
                print("your balance is ",amount)
        else:
            print("invalid pin ")
else: print("invalid card")


