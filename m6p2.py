partnumber = input("Enter the part number: ")
quantity = input("Enter the quantity: ")

if partnumber == "10" or partnumber == "55":
    unitcost = 1.00
elif partnumber == "99":
    unitcost = 2.00
elif partnumber == "80" or partnumber == "70":
    unitcost = 3.00
else:
    unitcost = 5.00

totalcost = unitcost * unitcost

print(f"{'Part Number':<12} {'Unit Cost':>10} {'Total Cost':>12}")
print(f"{partnumber:<12} ${unitcost:>9.2f} ${totalcost:>11.2f}")
