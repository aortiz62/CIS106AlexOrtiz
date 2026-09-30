quantity = int(input("Enter quantity: "))

if quantity > 10000:
    price = 10
elif quantity >= 5000:
    price = 20
else:
    price = 30

extendedprice = quantity * price
tax = extendedprice * 0.07
total = extendedprice + tax

print(f"Extended Price: ${extendedprice:>12.2f}")
print(f"Tax Amount:     ${tax:>12.2f}")
print(f"Total:          ${total:>12.2f}")