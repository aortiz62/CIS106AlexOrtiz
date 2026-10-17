totaltuition = 0.0
studentcount = 0

with open("students.txt", "r") as file:
    lines = [line.strip() for line in file if line.strip()]

for i in range(0, len(lines), 3):
    lastname = lines[i]
    districtcode = lines[i+1]
    creditstaken = int(lines[i+2])

    if districtcode == "I":
        tuition = creditstaken * 250.00
    else:
        tuitionowed = creditstaken * 500.00

    totaltuition += tuitionowed
    studentcount += 1

    print(f"total tuition owed: ${tuitionowed:.2f}")
    print(f"total students: {studentcount}")