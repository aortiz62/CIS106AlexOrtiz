def main():
    students = {
        "Smith": 88,
        "Johnson": 92,
        "Williams": 79,
        "Brown": 95,
        "Jones": 84,
        "Garcia": 91,
        "Miller": 76,
        "Davis": 89,
        "Rodriguez": 94,
        "Martinez": 82
    }

    print("{:<15} {:<10}".format("Student Name", "Grade"))
    print("-" * 25)

    total = 0
    for name, grade in students.items():
        print("{:<15} {:<10}".format(name, grade))
        total += grade

    average = total / len(students)

    print("-" * 25)
    print("{:<15} {:<10.2f}".format("Class Average", average))

main()
