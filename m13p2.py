def calculate_student_averages(grade_dict):
    student_averages = []
    for name, grades in grade_dict.items():
        avg = sum(grades) / len(grades)
        student_averages.append(list((name, avg)))
    return student_averages
