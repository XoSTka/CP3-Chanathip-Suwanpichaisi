inputTotalPrice = float(input("Price : "))
def vatCalculate(inputTotalPrice):
    result = inputTotalPrice + (inputTotalPrice * 7 / 100)
    return result
print("Total : " + str(vatCalculate(inputTotalPrice)))