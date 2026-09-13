stockticker = input("Enter stock ticker symbol: ")
stockticker_symbol = "MSFT"

number_of_shares = int(input("Enter the number of shares: "))
cost_per_share = float(input("Enter the cost per share: "))
amount_invested = float(input("Enter the amount you want to invest ($): "))

amount_invested = number_of_shares * cost_per_share
print(f"The amount invested is: ${amount_invested:,.2f}")