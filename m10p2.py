def computewallarea(length, width, height):
    return 2 * length * height + 2 * width * height

def computeflatarea(length, width):
    return length * width

def main():
    runagain = input("do you want to enter a room?: ")
    while runagain.lower() == "yes" or runagain.lower() == "Yes":
        length = float(input("enter length: "))
        width = float(input("enter width: "))
        height = float(input("enter height: "))
        
        wallarea = computewallarea(length, width, height)
        flatarea = computeflatarea(length, width)
        
        wallgallons = wallarea / 50
        ceilinggallons = flatarea / 50
        floorvarnishgallons = flatarea / 50
        
        print("wall square footage:", wallarea)
        print("gallons of wall paint:", wallgallons)
        print("ceiling or floor area:", flatarea)
        print("gallons of ceiling paint:", ceilinggallons)
        print("gallons of floor varnish:", floorvarnishgallons)
        
        runagain = input("do you want to enter another room?")
