# concession stand game 



menu = {'popcorn': 3.40,
        'pizza' : 4.21,
        'chips' : 5.21,
        'soda' : 6.21,
        'fries' : 7.21,
        'lemonade' : 1.21,
        'pretzel' : 2.21,
        'chawarma' : 3.51,
        'sambusa' : 4.77,

        }

cart =[]
total =0

# for  key, value in menu.items():
#     print(f'{key:8} : ${value:.2f}')

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
for food in cart:
    total += menu[food]
    print(food, end=' ')

print(f'{total:.2f}')