def ComputeTuition(credits, district):
    if district == "I" or district == "i":
        tuition = credits * 250.0
    elif district == "O" or district == "o":
        tuition = credits * 550.0
    else:
        tuition = 0.0
    return tuition

totalTuition = 0

lastName = input()
while lastName != "exit":
    creditHours = int(input())
    districtCode = input()
    tuitionOwed = ComputeTuition(creditHours, districtCode)
    totalTuition = totalTuition + tuitionOwed
  
    print(lastName)
    print(tuitionOwed)
   
    lastName = input()

print(totalTuition)