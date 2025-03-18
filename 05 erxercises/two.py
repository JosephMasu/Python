# Exercise 2 shopping Cart Program


items = input('What item would you like to buy?: ')
price = float(input('What is the price of the item?: '))
quantity = int(input('How many would you want to buy?: '))

total = price * quantity

print(f'you have bought {quantity} {items} for ${total:.4f}')
