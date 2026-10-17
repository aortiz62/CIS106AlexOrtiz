principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))

totalinterest =  0.0

for year in range(1,6):
    interest = principal * rate
    endingbalance = principal + interest
    totalinterest += interest

    print(f"Year {year}: principal: {principal:.2f}, endingbalance: {endingbalance:.2f}")

print(f"your total interest is: {totalinterest:.2f}")