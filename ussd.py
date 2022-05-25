# ASSIGNMENT
# 1. USSD with function...
secpin = "*123#"
pin = input("Enter your pin>>")
def ussd(pin):
    if pin == secpin:
        print("1. Buy credit\n2. Buy Data\n3. Borrow Airtime")
    else:
        print('USSD Error!')
        quit()

    choose = input("Enter any number>>")
    if choose == "1":
        print("1. #1000\n2. #500\n3. #100")
        
        choose = input("Enter any number>>")
        if choose == "1":
            print("You have successfully purchased #1000 airtime")
        elif choose == '2':
            print("You have successfully purchased #500 airtime")
        elif choose == '3':
            print("You have successfully purchased #100 airtime")
        else:
            print("Wrong Entry")
    
    elif choose == '2':
        print("1. 500 Mb for #500\n2. 1 GB for # 1000")

        choose = input("Enter any number>>")
        if choose == '1':
            print("Your purchase of 500 Mb data was successful")
        elif choose == '2':
            print("Your purchase of 1 GB data was successful")
        else:
            print("Wrong Entry")
    
    elif choose == '3':
        print("This service attracts charge of 10 per cent.\n Choose:\n1. To continue\n2. To cancel")
        choose = input("Enter any number>>")
        if choose == '1':
            print("1. #100\n2. #200\n3. #400")
            choose = input("Enter any number>>")
            if choose == '1':
                print("Your account has been credited #100. A charge of #10 has been deducted")
            elif choose == '2':
                print("Your account has been credited #200. A charge of #20 has been deducted")
            elif choose == '3':
                print("Your account has been credited #400. A charge of #40 has been deducted")
            else:
                print("Wrong Entry")
        elif choose == '2':
            print("Process cancelled")
        else:
            print("Wrong Entry")
    else:
        print("Wrong Entry")

ussd(pin)