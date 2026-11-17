def calculate_student_averages(grade_dict):
    student_averages = []
    for name, grades in grade_dict.items():
        avg = sum(grades) / len(grades)
        student_averages.append(list((name, avg)))
    return student_averages

def main():
    students = {
        "Smith": (88, 90, 85),
        "Johnson": (92, 89, 94),
        "Williams": (79, 82, 80),
        "Brown": (95, 93, 97),
        "Jones": (84, 86, 81),
        "Garcia": (91, 88, 90),
        "Miller": (76, 79, 75),
        "Davis": (89, 91, 87),
        "Rodriguez": (94, 92, 96),
        "Martinez": (82, 85, 80)
    }

averages_list = calculate_student_averages(students)

    print(f"{'Student Name':<15} {'Average Grade':<15}")
    print("-" * 30)
    for item in averages_list:
        name = item.pop(0)
        avg = item.pop(0)
        print(f"{name:<15} {avg:<15.2f}")

print("\n" + "=" * 30 + "\n")

    num_students = len(students)
    grade1_total = 0
    grade2_total = 0
    grade3_total = 0

    for g1, g2, g3 in students.values():
        grade1_total += g1
        grade2_total += g2
        grade3_total += g3

    print(f"{'Assignment':<15} {'Class Average':<15}")
    print("-" * 30)
    print(f"{'Grade 1':<15} {grade1_total / num_students:<15.2f}")
    print(f"{'Grade 2':<15} {grade2_total / num_students:<15.2f}")
    print(f"{'Grade 3':<15} {grade3_total / num_students:<15.2f}")

main()
