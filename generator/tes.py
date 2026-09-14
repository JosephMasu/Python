import report
import pcost

portfolio = report.read_portfolio("portfolio.csv")

print("Total cost:", portfolio.total_cost)

print("Shares:", portfolio.tabulate_shares())

print("Stocks:")

for stock in portfolio:
    print(stock.name, stock.shares, stock.price)

print("Using pcost:", pcost.portfolio_cost("portfolio.csv"))