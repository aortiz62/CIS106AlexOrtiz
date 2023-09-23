#input 
unitprice = input("enter the unit price")
qty = input("enter the quantity")
total = input("total price")
#process
if qty>=1000:
    up = 3.00
else:
    up = 5.00

total = qty * unitprice

#output
print("what is the quantity")
print("the total is $" &total)