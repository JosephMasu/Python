#Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. The interest rate is 5% and the monthly payment is $2684.11.
# mortage_life = 30  # Mortgage life in years
# mortage_amount = 500000  # Principal amount of the mortgage
# monthly_payment = 2684.11  # Monthly payment amount
# monthly_rate = 5/100


# # Calculate the total amount paid over the life of the mortgage
# while mortage_amount > 0:
#     mortage_amount += mortage_amount * monthly_rate / 12  # Add interest for the month
#     mortage_amount -= monthly_payment 
#     print("Remaining mortgage amount: ${:.2f}".format(mortage_amount))

# print("Total amount paid over the life of the mortgage: ${:.2f}".format(monthly_payment * 12 * mortage_life))

# Suppose Dave pays an extra $1000/month for the first 12 months of the mortgage?

# Modify the program to incorporate this extra payment and have it print the total amount paid along with the number of months required.


# Initial mortgage details
principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

total_paid = 0.0
months = 0

# Print table header
print(f"{'Month':<10}{'Total Paid':<15}{'Remaining Principal':<20}")

# Loop until the mortgage is paid off
while principal > 0:
    # Determine the monthly payment
    if extra_payment_start_month <= months + 1 <= extra_payment_end_month:
        monthly_payment = payment + extra_payment
    else:
        monthly_payment = payment

    # Don't pay more than what is owed
    if monthly_payment > principal:
        monthly_payment = principal

    # Update principal, total paid, and months
    principal = principal + (principal * rate / 12) - monthly_payment
    total_paid += monthly_payment
    months += 1

    # Print the current month's details
    print(f"{months:<10}{round(total_paid, 2):<15}{round(principal, 2):<20}")

# Final summary
print("\nTotal paid:", round(total_paid, 2))
print("Months:", months)