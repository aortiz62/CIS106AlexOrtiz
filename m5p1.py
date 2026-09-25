quantityinput = input("Enter the quantity: ")
quantity = int(quantityinput)

if quantity >=1000:
    unitprice = 3.00
else:
    unitprice = 5.00

extendedprice = quantity * unitprice
tax = extendedprice * 0.07
total = extendedprice + tax

print(f"Quantity: {quantity}")
print(f"Unit price: ${unitprice:.2f}")
print(f"Extended price: ${extendedprice:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")