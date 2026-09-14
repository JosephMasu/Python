from stock import Stock
from portfolio import Portfolio


def read_portfolio(filename):
    holdings = []

    with open(filename) as f:
        next(f)  # skip header

        for line in f:
            name, shares, price = line.split(',')

            stock = Stock(
                name,
                int(shares),
                float(price)
            )

            holdings.append(stock)

    return Portfolio(holdings)