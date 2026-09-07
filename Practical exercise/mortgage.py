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


principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    print('Remaining principal', principal)

print('Total paid', total_paid)
