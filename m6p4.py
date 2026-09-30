tickets = int(input("Enter amount of tickets: "))

if tickets >= 25:
    price = 50
elif tickets >= 10:
    price = 60
elif tickets >= 5:
    price = 70
else:
    price = 75

total = tickets * price

print("Number of tickets:", tickets)
print("Price of each ticket: $", price)
print("Total cost: $", total)