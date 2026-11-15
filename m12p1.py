names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

def display_names(name_list):
    for i in range(len(name_list)):
        print(name_list[i])

def display_names_reversed(name_list):
    for i in range(len(name_list) - 1, -1, -1):
        print(name_list[i])

if __name__ == "__main__":
    display_names(names)
    display_names_reversed(names)