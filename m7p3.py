studentcount = 0

continuechoice = input("Do you want to continue? enter yes to continue ")

while continuechoice.lower() == "yes":
    studentcount += 1

    lastname = input("Enter the last name")
    exam1 = float(input("Enter the first exam score"))
    exam2 = float(input("Enter the second exam score"))

    average = (exam1 + exam2) / 2
    print("The average score for", lastname, "is", average)

    continuechoice = input("Do you want to continue? enter yes to continue ")

print("The total number of students is", studentcount)