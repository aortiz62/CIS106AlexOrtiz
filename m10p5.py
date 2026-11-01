def computeassessedvalue(county, marketvalue):
    if county.lower() == "cook":
        percent = 0.90
    elif county.lower() == "dupage":
        percent = 0.80
    elif county.lower() == "mchenry":
        percent = 0.75
    elif county.lower() == "kane":
        percent = 0.60
    else:
        percent = 0.70
    return marketvalue * percent

totalmarketvalue = 0
totalassessedvalue = 0
response = input("do you want to enter a home? ")

while response.lower() == "yes":
    county = input("enter county: ")
    marketvalue = float(input("enter market value: "))
    
    assessedvalue = computeassessedvalue(county, marketvalue)
    
    totalmarketvalue = totalmarketvalue + marketvalue
    totalassessedvalue = totalassessedvalue + assessedvalue
    
    print("assessed value for this home is " + str(assessedvalue))
    response = input("do you want to enter another home? ")

print("total market value of all homes: " + str(totalmarketvalue))
print("total assessed value of all homes: " + str(totalassessedvalue))