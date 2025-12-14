stock_prices={
    "AAPL": 150.25,
    "GOOGL": 2750.50,
    "MSFT": 299.00,
    "AMZN": 3400.75,
    "TSLA": 720.10    
}
totalinvestment=0
print("Stock Portfolio Prices:")
print("Available Stocks:",",".join(stock_prices.keys()))
numstocks=int(input("Enter number of different stocks you want to invest in: "))    
for i in range(numstocks):
    stockname=input(f"Enter the stock name for stock {i+1}: ").upper()
    if stockname in stock_prices:
        quantity=int(input(f"Enter the quantity of {stockname} you want to buy: "))
        stockcost=stock_prices[stockname]*quantity
        totalinvestment+=stockcost
    else:
        print(f"Stock {stockname} is not available in the portfolio.") 
print(f"Total investment amount: ${totalinvestment:.2f}")
         
