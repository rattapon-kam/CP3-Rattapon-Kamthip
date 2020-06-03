username = "admin"
password = "admin1234"
menu1 = 45
menu2 = 50
menu3 = 60
menu4 = 65
menu5 = 55
if input("Please Enter Username : ") == username and input("Please Enter Password : ") == password:
    print("-----Welcome to Python Cafe-----")
    print("1.Cappuccino                 45 THB ")
    print("2.Mocha                      50 THB ")
    print("3.Latte                      60 THB ")
    print("4.White Choc Macchiato       65 THB ")
    print("5.Americano                  55 THB ")
    menu = int(input("Please Enter Menu(1-5) : "))
    number = int(input("Please Enter Number : "))
    if menu == 1:
        total = menu1*number
    elif menu == 2:
        total = menu2*number
    elif menu == 3:
        total = menu3*number
    elif menu == 4:
        total = menu4*number
    elif menu == 5:
        total = menu5*number
    print("Total :",total,"THB")
else:print("Login Fail !!!")