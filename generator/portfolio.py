# On occasion, you might want to make one of your own objects support iteration--especially if your object wraps around an existing list or other iterable. In a new file portfolio.py, define the following class:

# portfolio.py

class Portfolio:

    def __init__(self, holdings):
        self._holdings = holdings

    def __iter__(self):
        return iter(self._holdings)

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter
        total_shares = Counter()

        for s in self._holdings:
            total_shares[s.name] += s.shares

        return total_shares