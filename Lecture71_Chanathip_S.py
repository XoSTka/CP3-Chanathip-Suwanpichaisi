menuList = []
priceList = []
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)

def showBill():
    print("---- My Food----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        totalPrice += priceList[number]
    print("Total : ", totalPrice)

showBill()




