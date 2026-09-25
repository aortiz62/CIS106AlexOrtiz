numberbooks = int(input("Enter the number of books: "))
costperbook = float(input("Enter the cost per book: "))

ordertotal = numberbooks * costperbook

if ordertotal > 50.00:
    shippingcharge = 0.00
else:
    shippingcharge = 25.00

print(f"Order total: ${ordertotal:.2f}")
print(f"shipping charge: ${shippingcharge:.2f}")