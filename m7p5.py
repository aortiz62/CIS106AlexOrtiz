sumdiscount = 0

continuechoice = input("Do you want to run the program? type yes to continue")

while continuechoice.lower() == "yes":

    quantity = int(input("Enter the quantity of items purchased: "))
    price = float(input("Enter the price of the item: "))

    extprice = quantity * price

    if extprice > 10000:
        discountrate = 0.25
    else:
        discountrate = 0.10

    discountamt = extprice * discountrate
    total = extprice - discountamt

    sumdiscount = sumdiscount + discountamt

    print(f"Extended price: ${extprice:.2f}")
    print(f"Discount amount: ${discountamt:.2f}")
    print(f"Total amount: ${total:.2f}")

    continuechoice = input("Do you want to continue running the program loop? type yes to continue")

    print(f"Total discount amount: ${sumdiscount:.2f}")