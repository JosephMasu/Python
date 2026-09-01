import random

options = ['rock', 'paper', 'scissors']

print('---------- Your Game Has Started ----------')

while True:
    player1 = input("player1: Enter your choice (rock, paper, scissors or 'quit' to exit): ").lower()

    if player1 == 'quit':
        print('Game Over. Thanks for playing!')
        break

    if player1 not in options:
        print('Invalid choice. Please choose rock, paper, or scissors.')
        continue

    player2 = random.choice(options)
    print(f'player2: {player2}')

    if player1 == player2:
        print('It\'s a tie!')
    elif (player1 == 'rock' and player2 == 'scissors') or \
         (player1 == 'scissors' and player2 == 'paper') or \
         (player1 == 'paper' and player2 == 'rock'):
        print('player1 wins!')
    else:
        print('player2 wins!')