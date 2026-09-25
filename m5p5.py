lastname = input("Enter your last name: ")
grossincome = float(input("Enter your gross income: "))
dependents = int(input("Enter the number of dependents: "))

adjgrossincome = grossincome - (dependents * 12000)

if adjgrossincome > 500000:
    incometax = adjgrossincome * .20
else:
    incometax = adjgrossincome * .10

if incometax < 0:
    incometax = 100.0

print(f"last name: {lastname}")
print(f"gross income: ${grossincome:.2f}")
print(f"number of dependents: {dependents}")
print(f"adjusted gross income: ${adjgrossincome:.2f}")
print(f"income tax: ${incometax:.2f}")