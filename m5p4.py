appliancename = input("Enter the appliance name: ")
appliancecost = float(input("Enter the appliance cost: "))

if appliancecost > 1000:
    warrantycost = appliancecost * 0.10
else:
    warrantycost = appliancecost * 0.05

totalcost = appliancecost + warrantycost
print(f"appliance name: {appliancename}")
print(f"appliance cost: ${appliancecost:.2f}")
print(f"warranty cost: ${warrantycost:.2f}")
print(f"total cost: ${totalcost:.2f}")