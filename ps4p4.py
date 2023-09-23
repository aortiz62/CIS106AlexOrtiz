#input
warrantee = input("enter warrantee cost")
appliances = input("cost of appliances")
totalcost = input("the total cost of appliances and warrantee")
#process
if appliances>=1000:
    up = 5/100*1000
else:
    up = 10/100*1000
#output
print("cost of the appliances")
print("cost of warrantee + appliances $" &totalcost)