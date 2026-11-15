names = []
scores = []

with open("students.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        names.append(data[0])
        scores.append(int(data[1]))

def display_high_low(name_list, score_list):
    high_var = 0
    high_index = 0
    low_var = 999
    low_index = 0
    
    for i in range(len(score_list)):
        if score_list[i] > high_var:
            high_var = score_list[i]
            high_index = i
            
        if score_list[i] < low_var:
            low_var = score_list[i]
            low_index = i
            
    print(name_list[high_index], high_var)
    print(name_list[low_index], low_var)

if __name__ == "__main__":
    display_high_low(names, scores)