totalgross = 0
empcount = 0

continuechoice =  input("Do you want to run the program? type yes to continue")

while continuechoice == "yes":
    lastname = input("Enter the employee's last name: ")
    hours = float(input("Enter the number of hours worked: "))
    rate = float(input("Enter the hourly pay rate: "))

    if hours > 40:
        grosspay = (40 * rate) + ((hours - 40) * (rate * 1.5))
    else:
        grosspay = hours * rate

    totalgross += grosspay
    empcount += 1

    print(f"{lastname}'s gross pay is: ${grosspay:.2f}")

    continuechoice = input("Do you want to run the program again? type yes to continue")

    if empcount > 0:
        avgpay = totalgross / empcount
        print(f"total employees: {empcount}")
        print(f"total gross pay: ${totalgross:.2f}")
        print(f"average gross pay: ${avgpay:.2f}")