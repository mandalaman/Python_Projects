with open("currencyData.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter the amount: "))
print("Enter the name of currency you want to convert this amount? available options: /n")
[print(item) for item in currencyDict.keys()]
currency = input("please enter one of these values: \n")
print(f"{amount} INR is equal to {amount * float(currencyDict[currency])} {currency}")

