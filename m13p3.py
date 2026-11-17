def print_players(player_dict):
    print("{:<15} {:<12}".format("Player Name", "Batting Avg"))
    print("-" * 27)
    for name, avg in player_dict.items():
        print("{:<15} {:<12.3f}".format(name, avg))

def main():
    players = {}

    with open("players.txt", "r") as file:
        while True:
            name_line = file.readline()
            if not name_line:
                break
            avg_line = file.readline()
            name = name_line.strip()
            avg = float(avg_line.strip())
            players[name] = avg

    print_players(players)

main()
