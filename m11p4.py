def getaverage(game1, game2, game3):
    avg = (game1 + game2 + game3) / 3
    return avg

def gethandicapaverage(scratchavg, handicap):
    handicapavg = scratchavg + handicap
    return handicapavg

lastname = input()
game1 = float(input())
game2 = float(input())
game3 = float(input())
handicap = float(input())

average = getaverage(game1, game2, game3)
handicapaverage = gethandicapaverage(average, handicap)

print(lastname)
print(average)
print(handicapaverage)