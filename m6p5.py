lastname = input("Enter your last name: ")
salary = float(input("Enter your salary: "))
joblvl = int(input("Enter job level: "))

if joblvl >= 10:
    bonus_rate = 0.25
elif joblvl >= 5:
    bonusrate = 0.20
else:
    bonusrate = 0.10

bonus = salary * bonusrate

print(f"Employee: {lastname}")
print(f"Bonus amount is: ${bonus:,.2f}")