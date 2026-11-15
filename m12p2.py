names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
scores = [85, 92, 78, 99, 62, 88, 74, 91, 55, 83]

def display_student_data(name_list, score_list):
    for i in range(len(name_list)):
        print(name_list[i], score_list[i])

def display_student_data_reversed(name_list, score_list):
    for i in range(len(name_list) - 1, -1, -1):
        print(name_list[i], score_list[i])

if __name__ == "__main__":
    display_student_data(names, scores)
    display_student_data_reversed(names, scores)