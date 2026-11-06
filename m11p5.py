total = 0.0
tax = 0.0

def calcbill(qty, price):
    global total
    global tax
    total = qty * price
    tax = total * 0.07

qty = float(input())
price = float(input())

calcbill(qty, price)

print(total)
print(tax)