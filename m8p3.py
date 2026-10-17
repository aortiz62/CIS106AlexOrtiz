with open ("employees.txt", "w") as file:
    file.write("Adam\n120000.00\nBaker\n50000.00\nSmith\n45000.00\n")

totalbonuses = 0.0

with open ("employees.txt", "r") as file:
    while True:
        line1 = file.readline()
        if not line1:
            break
        lastname = line1.strip()

        line2 = file.readline()
        salary = float(line2.strip())

        if salary >= 100000.00:
            bonus = salary * 0.20
        elif salary >= 50000.00:
            bonus = salary * 0.15
        else:
            bonus = salary * 0.10

        totalbonuses += bonus
        print(f"{lastname} total bonus is ${bonus:.2f}")