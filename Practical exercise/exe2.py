#Pro-tip: Use the underscore (_) variable to use the result of the last calculation. For example, how much profit does Larry make after his evil broker takes their 20% cut?

# Prompt the user for input
profit = float(input("Enter the profit Larry made from selling all his shares: "))
# Calculate profit after broker's cut
broker_cut = profit * 0.20
_ = profit - broker_cut

# Print the profit after broker's cut
print("Larry's profit after the broker's 20% cut is: $", _)