def ComputeMPG(miles, gallons):
    if gallons == 0:
        mpg = 0.0
    else:
        mpg = miles / gallons
    return mpg

tripCount = 0

city = input()
while city != "exit":
    miles = float(input())
    gallons = float(input())
    mpg = ComputeMPG(miles, gallons)
    tripCount = tripCount + 1
    
    print(city)
    print(miles)
    print(mpg)
    
    city = input()

print(tripCount)