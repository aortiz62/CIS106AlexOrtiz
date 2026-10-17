totalextendedprice = 0.0
ordercount = 0

with open('orders.txt', 'r') as file:
    lines = [line.strip() for line in file if line.strip()]

for i in range(0, len(lines), 3):
    item = lines[i]
    quantity = int(lines[i+1])
    price = float(lines[i+2])

    extendedprice = quantity * price
    totalextendedprice += extendedprice
    ordercount += 1

    print(f"Item: {item}, Qty: {quantity}, Price: {price:.2f}, Extended Price: {extendedprice:.2f}")

averageorder = totalextendedprice / ordercount if ordercount > 0 else 0.0

print(f"total sales: {totalextendedprice:.2f}")
print(f"total orders: {ordercount}")
print(f"average order: {averageorder:.2f}")