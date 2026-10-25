def ComputeTotal(qty, price):
    total = qty * price
    if total > 10000.00:
        total = total * 0.90
    return total

extendedTotal = 0

qty = float(input())
while qty != 0:
    price = float(input())
    itemTotal = ComputeTotal(qty, price)
    extendedTotal = extendedTotal + itemTotal
    
    print(qty)
    print(price)
    print(itemTotal)
    
    qty = float(input())

print(extendedTotal)