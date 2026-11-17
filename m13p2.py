def calculate_student_averages(grade_dict):
    student_averages = []
    for name, grades in grade_dict.items():
        avg = sum(grades) / len(grades)
        student_averages.append([name, avg])
    return student_averages

def main():
    students = {
        "Smith":,
        "Johnson":,
        "Williams":,
        "Brown":,
        "Jones":,
        "Garcia":,
        "Miller":,
        "Davis":,
        "Rodriguez":,
        "Martinez": [82, 85, 80]
    }

    averages_list = calculate_student_averages(students)

    print("{:<15} {:<15}".format("Student Name", "Average Grade"))
    print("-" * 30)
    for item in averages_list:
        print("{:<15} {:<15.2f}".format(item[0], item[1]))

    print()

    num_students = len(students)
    grade1_total = 0
    grade2_total = 0
    grade3_total = 0

    for grades in students.values():
        grade1_total += grades[0]
        grade2_total += grades[1]
        grade3_total += grades[2]

    print("{:<15} {:<15}".format("Assignment", "Class Average"))
    print("-" * 30)
    print("{:<15} {:<15.2f}".format("Grade 1", grade1_total / num_students))
    print("{:<15} {:<15.2f}".format("Grade 2", grade2_total / num_students))
    print("{:<15} {:<15.2f}".format("Grade 3", grade3_total / num_students))

main()
