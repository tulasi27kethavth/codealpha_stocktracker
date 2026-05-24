# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 188,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 320
}

total_investment = 0
portfolio = {}

# Number of stocks user wants to enter
n = int(input("Enter number of stocks: "))

# Taking user input
for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    # Check if stock exists
    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        portfolio[stock_name] = quantity
    else:
        print("Stock not found!")

# Display portfolio details
print("\n--- Portfolio Summary ---")

for stock, qty in portfolio.items():
    print(f"{stock} : {qty} shares × ${stock_prices[stock]}")

print(f"\nTotal Investment Value = ${total_investment}")

# Optional: Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("--- Portfolio Summary ---\n")

    for stock, qty in portfolio.items():
        file.write(f"{stock} : {qty} shares × ${stock_prices[stock]}\n")

    file.write(f"\nTotal Investment Value = ${total_investment}")

print("\nPortfolio saved to portfolio.txt")