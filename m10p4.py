def computeticketprice(miles):
    if miles >= 30:
        return 12
    elif miles >= 20:
        return 10
    elif miles >= 10:
        return 8
    else:
        return 5

totalprice = 0
response = input("do you want to enter a ticket?")

while response.lower() == "yes":
    lastname = input("enter last name: ")
    miles = float(input("enter miles: "))
    
    ticketprice = computeticketprice(miles)
    totalprice = totalprice + ticketprice
    
    print("ticket price for " + lastname + "is" + str(ticketprice))
    response = input("do you want to enter another ticket?")

print("the total price for all tickets is" + str(totalprice))