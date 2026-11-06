def calcdiscount(qty, price, rate):
    discountamount = qty * price * (rate / 100)
    discountedprice = (qty * price) - discountamount
    return discountamount, discountedprice

qty = float(input())
price = float(input())
rate = float(input())

discountamount, discountedprice = calcdiscount(qty, price, rate)

print(qty)
print(price)
print(rate)
print(discountamount)
print(discountedprice)