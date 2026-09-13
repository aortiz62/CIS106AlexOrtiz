
totalamount = float(input("Enter the amount received: $"))
numberofpeople = int(input("Enter the number of people: "))

amountshared = totalamount / numberofpeople
print(f"Each person will receive: ${amountshared:.2f}")