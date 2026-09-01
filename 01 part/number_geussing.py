import random

top = (input('Enter the top number: '))

if top.isdigit():
    top = int(top)
    if top <= 0:
        print('Please enter a number greater than 0 next time.')
        quit()
else:
    print('Please enter a number next time.')
    quit()

r = random.randint(0, top)
guess1 = 0
while True:
    guess1 += 1
    guess = input('Make a guess: ')
    if guess.isdigit():
        guess = int(guess)

    else:
        print('Please enter a number next time.')
        continue

    if guess == r:
        print('You got it!')
        break
    elif guess < r:
            print('Too low!')

    else:
            print('Too high!')
print('You got it in ' + str(guess1) + ' guesses!')
