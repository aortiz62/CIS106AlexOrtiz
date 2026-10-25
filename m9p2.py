def Computeaverage(hits, atbats):
    if atbats == 0:
        avg = 0.0
    else:
        avg = hits / atbats
    return avg

playerCount = 0

lastName = input()
while lastName != "exit":
    hits = int(input())
    atbats = int(input())
    battingavg = Computeaverage(hits, atbats)
    playerCount = playerCount + 1
    
    print(lastName)
    print(battingavg)
    
    lastName = input()

print(playerCount)