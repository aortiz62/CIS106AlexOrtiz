def getcommission(sales):
    if sales > 100000:
        commision = sales * 0.10
    else:
        commission = sales * 0.05
    return commission

def gettarget(sales):
    target = sales * 0.05
    return target

lastname = input()
sales = float(input())

commission = getcommission(sales)
target = gettarget(sales)

print(lastname)
print(commission)
print(target)