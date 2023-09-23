#input
lname = input("enter last name")
numberofdependents = input("enter number of dependents")
gross = input("enter a gross sum")
#process
if gross >=50000:
    up = "tax rate plus 20%"
else:
    up = "tax rate of 10%"
#output
print("compute adjusted gross income minus dependents times 12000")
print("gross income under 50000 have tax rate of 10% $" &gross)
print("income over 50000 tax rate plus 20% $" &gross)
print("gross total income $" &gross)