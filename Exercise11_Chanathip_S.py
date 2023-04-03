userInputNumber = int(input("Number : "))
for x in range(userInputNumber):
    print((" "*(userInputNumber-x-1))+("*"+("*"*(x*2))))