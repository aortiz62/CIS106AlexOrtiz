#input
itemprice = input("enter item price")
qty = input("enter quantity")
unitprice = input("enter the unit price")
extprice = input("what is the extended price?")
#process
extprice = qty * itemprice

if itemprice>="A":
    up = 10.00
else:
    up = 20.00
#output
print("display unit price")
print("unit price of the item is $" &unitprice)