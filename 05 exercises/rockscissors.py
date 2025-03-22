import random

options = ('rock', 'scissors', 'paper')

print()
print('---------- Your Game Has Started----------')

player1 = input("player1: Enter your choice: ")
player2 = input("player2: Enter your choice: ")

if player1 not in options or player2 not in options:
    print('invalid choice')
    exit()

else:
    print(f'\n player1: {player1}')
    print(f'player2: {player2}')

if player1 == player2:
    print('tie')
    exit()
elif player1 == 'rock' and player2 == 'scissors' or player1 == 'scissors' and player2 == 'paper' or player1 == 'paper' and player2 == 'rock':
    print('player1 wins')
else:
    print('player2 wins')


# responce = random.choice(options)
# print(responce)