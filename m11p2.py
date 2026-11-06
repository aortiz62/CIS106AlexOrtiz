def gettotal(score1, score2, score3):
    total = score1 + score2 + score3
    return total

def getaverage(totalpoints):
    avg = totalpoints / 3
    return avg

lastname = input()
score1 = float(input())
score2 = float(input())
score3 = float(input())

total = gettotal(score1, score2, score3)
average = getaverage(total)

print(lastname)
print(total)
print(average)