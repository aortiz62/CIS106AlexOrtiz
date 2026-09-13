make = str(input("enter make of car: "))
model = str(input("enter model of car: "))
msrpamount = float(input("enter msrp amount: "))
discountpercent = float(input("enter discount percent: "))

amountoff = msrpamount * (discountpercent / 100)
discountedprice = msrpamount - amountoff