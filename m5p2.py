item = input("Enter an item (a or b): ")
quantity = int(input("Enter the quantity: "))

if item == "a":
    unitprice = 10.00
else:
    unitprice = 20.00

extendedprice = quantity * unitprice

print(f"Item: {item}")
print(f"unitprice: {unitprice:.2f}")
print(f"extendedprice: {extendedprice:.2f}")