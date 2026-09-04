from requests import get

BASE_URL = "https://api.frankfurter.app"


def get_currencies():
    url = f"{BASE_URL}/currencies"
    response = get(url, timeout=20)

    if response.status_code != 200:
        print(f"API error {response.status_code}: {response.text}")
        return []

    data = response.json()
    currencies = [(code, {"id": code, "currencyName": name}) for code, name in data.items()]
    currencies.sort()
    return currencies


def print_currencies(currencies):
    for code, currency in currencies:
        print(f"{code} - {currency['currencyName']}")


def exchange_rate(currency1, currency2):
    url = f"{BASE_URL}/latest"
    response = get(
        url,
        params={"from": currency1, "to": currency2},
        timeout=20,
    )

    if response.status_code != 200:
        print("Invalid currencies.")
        return

    data = response.json()
    rates = data.get("rates", {})
    rate = rates.get(currency2)

    if rate is None:
        print("Invalid currencies.")
        return

    print(f"{currency1} -> {currency2} = {rate}")
    return rate


def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount


def main():
    currencies = get_currencies()
    if not currencies:
        print("Could not load currencies. Check your internet connection.")
        return

    print("Welcome to the currency converter!")
    print("List - lists the different currencies")
    print("Convert - convert from one currency to another")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")


main()
