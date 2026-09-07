# Lucky Larry bought 75 shares of Google stock at a price of $235.14 per share. 
# Today, shares of Google are priced at $711.25. Using Python’s interactive mode as a calculator, 
# figure out how much profit Larry would make if he sold all of his shares.

# Prompt the user for input
current_price = float(input("Enter the current price of Google stock: "))
purchase_price = float(input("Enter the purchase price of Google stock: "))
number_of_shares = int(input("Enter the number of shares Larry bought: "))

# Calculate profit
profit = (current_price - purchase_price) * number_of_shares

# Print the profit
print("Larry's profit from selling all his shares is: $", profit)