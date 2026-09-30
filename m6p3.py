principal = float(input("Enter principal amount: "))
years = int(input("Enter years: "))

if principal > 100000 and years == 5:
    interestrate = 0.06
elif 50000 <= principal <= 100000 and years == 10:
    interestrate = 0.05
elif 50000 <= principal <= 100000 and years == 5:
    interestrate = 0.04
else:
    interestrate = 0.02

firstyearinterest = principal * interestrate