def calculate_breakevenpoint():
    print("This calculates the breakevenpoint")

fixedcosts = float(input("Enter the fixed costs: "))
priceperunit = float(input("Enter the price per unit: "))
costperunit = float(input("Enter the cost per unit: "))

print("enter the total costs: ", fixedcosts)
print("enter the price per unit: ", priceperunit)
print("enter the cost per unit: ", costperunit)

breakevenpoint = fixedcosts / (priceperunit - costperunit)

print("must sell", breakevenpoint, "to break even")