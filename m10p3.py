def computeoutthedoor(msrp, make, model, iselectric):
    if iselectric.lower() == "y":
        discountpercent = 0.30
    elif make.lower() == "honda" and model.lower() == "accord":
        discountpercent = 0.10
    elif make.lower() == "toyota" and model.lower() == "rav4":
        discountpercent = 0.15
    else:
        discountpercent = 0.05
    discountedmsrp = msrp - (msrp * discountpercent)
    return discountedmsrp * 1.07

def main():
    totalmsrp = 0.0
    totalsaleprice = 0.0
    runagain = input("do you want to enter a car?")
    while runagain.lower() == "yes" or runagain.lower() == "y":
        make = input("enter make: ")
        model = input("enter model: ")
        iselectric = input("is it an electric vehicle?")
        msrp = float(input("enter msrp: "))
        
        saleprice = computeoutthedoor(msrp, make, model, iselectric)
        totalmsrp = totalmsrp + msrp
        totalsaleprice = totalsaleprice + saleprice
        
        print("out the door price:", saleprice)
        
        runagain = input("do you want to enter another car?")
        
    print("sum of all msrps:", totalmsrp)
    print("sum of all sales prices:", totalsaleprice)