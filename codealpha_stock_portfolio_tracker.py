stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 200
}

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks")

for stock, price in stock_prices.items():
    print(stock, ":", price)

portfolio = {}
total_investment = 0

num_stocks = int(input("\nHow many stocks do you want to buy? "))

for i in range(num_stocks):

    print("\nStock", i + 1)

    stock_name = input("Enter Stock Name: ").upper()
    quantity = int(input("Enter Quantity: "))

    if stock_name in stock_prices:

        investment = stock_prices[stock_name] * quantity

        portfolio[stock_name] = {
            "Quantity": quantity,
            "Price": stock_prices[stock_name],
            "Investment": investment
        }

        total_investment += investment

        print("Added Successfully!")

    else:
        print("Stock Not Available!")

print("\n===================================")
print("       PORTFOLIO SUMMARY")
print("===================================")

for stock, details in portfolio.items():
    print("\nStock:", stock)
    print("Quantity:", details["Quantity"])
    print("Price:", details["Price"])
    print("Investment:", details["Investment"])

print("\n-----------------------------------")
print("Total Investment Value =", total_investment)
print("-----------------------------------")

file = open("portfolio_report.txt", "w")

file.write("STOCK PORTFOLIO REPORT\n")
file.write("=========================\n")

for stock, details in portfolio.items():
    file.write(f"\nStock: {stock}\n")
    file.write(f"Quantity: {details['Quantity']}\n")
    file.write(f"Price: {details['Price']}\n")
    file.write(f"Investment: {details['Investment']}\n")

file.write(f"\nTotal Investment: {total_investment}")

file.close()

print("\nReport saved successfully in portfolio_report.txt")