purchaseprice = float(input("Enter the purchase price: "))
currentprice = float(input("Enter the current price: "))
quantity = int(input("Enter the quantity purchased: "))

value = (currentprice - purchaseprice) * quantity

if value > 0:
    print("you are earning more money:", value)
else:
    print("you are losing money.", value)