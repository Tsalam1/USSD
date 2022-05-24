# ASSIGNMENT
# 1. USSD with function...
secpin = "*123#"
pin = input("Enter your pin>>")
def ussd(pin):
    if pin == secpin:
        print("1. Buy credit\n2. Buy Data\n3. Borrow Credit")
    else:
        print('USSD Error')
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
            print("Wrong choice")
    
    elif choose == '2':
        print("1. 500 Mb for #500\n2. 1 GB for # 1000")
    # elif choose == '3':
    #     print("1. #50\n2. #100")
    # else:
    #     print('incorrect USSD')
    
    
ussd(pin)

# computerization1 = "1. Buy credit\n2. Buy Data\n3. Borrow Credit"

# computerization2 = "1. #1000\n2. #500\n3. #100"

# computerization3 = 