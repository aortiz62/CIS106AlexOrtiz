startval = float(input("Enter the start value: "))
stopval = float(input("Enter the stop value: "))
incrementval = float(input("Enter the increment value: "))

currentval = startval

if incrementval >= 0:
    while currentval <= stopval:
        print(currentval)
        currentval += incrementval