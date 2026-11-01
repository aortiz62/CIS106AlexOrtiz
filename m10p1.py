def computeForecast():
    monthClean = month.strip().lower()[:3]
    if monthClean in ["jan", "feb", "mar"]:
        forecastPercent = 0.10
    elif monthClean in ["apr", "may", "jun"]:
        forecastPercent = 0.15
    elif monthClean in ["jul", "aug", "sep"]:
        forecastPercent = 0.20
    else:
        forecastPercent = 0.25
    return sales * (1 + forecastPercent)

response = input("Do you want to run the program?")

while response == "Yes" or response == "yes":
    lastName = input("Enter last name")
    month = input("Enter month")
    sales = float(input("Enter current sales"))
    
    forecastedSales = computeForecast()
    print("The forecasted sales are", forecastedSales)
    
    response = input("Do you want to run the program again?")