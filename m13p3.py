def print_players(player_dict):
    print(f"{'Player Name':<15} {'Batting Avg':<12}")
    print("-" * 27)
    for name, avg in player_dict.items():
        print(f"{name:<15} {avg:<12.3f}")

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
