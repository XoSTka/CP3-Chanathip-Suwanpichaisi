usernameInput = input("Username : ")
passwordInput = input("password : ")
if usernameInput == "min" and passwordInput == "2":
    print("---Login Succeed---")
    print(">>Welcome to ZIX shop<<")
    print("----Product List----")
    print("1:Potato Chips  : 20 THB")
    print("2:Pepsi         : 15 THB")
    print("3:Milk          : 60 THB")
    print("4:Candy         :  5 THB")
    print("5:Water         :  7 THB")
    userSelected = int(input("Choose your product : "))
    if userSelected == 1:
        amount = int(input("How many? : "))
        price = 20 * amount
    elif userSelected == 2:
        amount = int(input("How many? : "))
        price = 15 * amount
    elif userSelected == 3:
        amount = int(input("How many? : "))
        price = 60 * amount
    elif userSelected == 4:
        amount = int(input("How many? : "))
        price = 5 * amount
    elif userSelected == 5:
        amount = int(input("How many? : "))
        price = 7 * amount
    elif userSelected < 1 or userSelected > 5:
        print("!Error!")
    else:
        print("Total :",price,"THB")
else:
    print("---Login Failed---")

