def GetPayRate(jobCode):
    if jobCode == "L" or jobCode == "l":
        rate = 25.0
    elif jobCode == "A" or jobCode == "a":
        rate = 30.0
    elif jobCode == "J" or jobCode == "j":
        rate = 50.0
    else:
        rate = 0.0
    return rate

totalGrossPay = 0

lastName = input()
while lastName != "exit":
    jobCode = input()
    hours = float(input())
    rate = GetPayRate(jobCode)
    
    if hours > 40:
        grossPay = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        grossPay = hours * rate
        
    totalGrossPay = totalGrossPay + grossPay
    
    print(lastName)
    print(grossPay)
    lastName = input()

print(totalGrossPay)