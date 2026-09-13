lastname = input("Enter last name: ")
midtermscore = float(input("Enter midterm score: "))
finalexamscore = float(input("Enter final exam score: "))

totalscore = (midtermscore * 0.40) + (finalexamscore * 0.60)

print(f"Student Last Name: {lastname}")
print(f"Total Exam Points: {totalscore:.2f}")