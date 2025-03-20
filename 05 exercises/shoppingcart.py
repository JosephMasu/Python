# shopping cart 


foods = []
prices = []
total = 0

while True:
    food = input('Enter the food you want to buy (q to quit): ')
    if food.lower() == 'q':
        break
    else:
        foods.append(food)
        price = float(input('Enter the price of the food: $'))
        prices.append(price)

print('--------- Your Cart ----------')
print(' ')

for food in foods:
    print(f'You bought {food} for $ {price}')

for price in prices:
    total += price
print('')
print(f'Your total is: ${total:.2f}')
