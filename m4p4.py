firstname = input("Enter your first name: ")
stepswalked = int(input("Enter thesteps you walked today: "))

caloriesburned = stepswalked * .25

print(f"{firstname}, the amount of calories you burned today is {caloriesburned:.2f}")