import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guess = 0
is_running = True

print('Python Number Guessing Game')
print(f'Guess a number between {lowest_num} and {highest_num}')

while is_running:
    guess = input('Enter your guess: ')

    if guess.isdigit():
        guess = int(guess)
        guess += 1
        
        if guess < lowest_num or guess > highest_num:
            print('Your guess number is out of range.')
            print(f'Please guess a number between {lowest_num} and {highest_num}')
        elif guess < answer:
            print('Your guess is too low.')
        elif guess > answer:
            print('Your guess is too high.')
        else:
            print(f'CORRECT! The answer was {answer}')
            print(f'Number of guesses: {guess}')
    
    else:
        print('Invalid guess.')
        print(f'Please guess a number between {lowest_num} and {highest_num}.')