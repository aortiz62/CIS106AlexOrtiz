#input
bookorders = input("number of books ordered")
cost = input("total cost of the books ordered")
totalcosts = input("total costs of orders and shipping charges")
#process

if cost>=50.00:
    up = "shipping free"
else:
    up = 25.00
#output
print("enter number of books to order and cost per book")
print("if cost is 50.00 or under charge 25.00 $" &cost)
print("if cost is greater than 50.00 shipping is free $" &cost)
print("order total and shipping charge $" &totalcosts)