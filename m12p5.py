names = []
averages = []

with open("players.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")
        names.append(data)
        averages.append(float(data))

def display_arrays(name_list, avg_list):
    for i in range(len(name_list)):
        print(name_list[i], avg_list[i])

def search_player(search_name, name_list, avg_list):
    found = False
    for i in range(len(name_list)):
        if name_list[i].lower() == search_name.lower():
            print(name_list[i], avg_list[i])
            found = True
    if not found:
        print("Name not found")

if __name__ == "__main__":
    display_arrays(names, averages)
    
    while True:
        user_search = input("Enter last name: ")
        if user_search == "":
            break
        search_player(user_search, names, averages)