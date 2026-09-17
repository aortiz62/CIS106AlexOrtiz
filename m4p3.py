mealtotal = float(input("Enter the total cost of the meal: "))

tip15 = mealtotal * .15
total15 = mealtotal + tip15

tip18 = mealtotal * .18
total18 = mealtotal + tip18

tip20 = mealtotal * .20
total20 = mealtotal + tip20

print(f"meal total: ${mealtotal:.2f}")
print(f"15% tip: ${tip15:.2f}")
print(f"total: ${total15:.2f}")
print() #break

print(f"meal total: ${mealtotal:.2f}")
print(f"18% tip: ${tip18:.2f}")
print(f"total: ${total18:.2f}")
print() #break

print(f"meal total: ${mealtotal:.2f}")
print(f"20% tip: ${tip20:.2f}")
print(f"total: ${total20:.2f}")