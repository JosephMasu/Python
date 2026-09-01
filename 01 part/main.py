#my first python program...

print('Joe has started Python')

playing = input('Do you want to play (yes/no): ')
if (playing!= 'yes'):
    quit()
print("Great! Let's play :)")

score = 0


answer = input('What is the capital of France? ')
if answer.lower() == 'paris':
    print('Correct!')
    score += 1
else:
    print('Incorrect! The answer is Paris.')

answer = input('what is your name? ')
if answer.lower() == 'masu':
    print('Correct!')
    score += 1

else:
    print('Incorrect! The answer is masu.')

answer = input('What is your age ? ')
if answer.lower() == '27':
    print('Correct!')
    score += 1

else:
    print('Incorrect! The answer is 27.')

answer = input('What is your major? ')
if answer.upper() == 'IT':
    print('Correct!')
    score += 1
else:
    print('Incorrect! The answer is IT.')

print('You got ' + str(score) + ' questions correct.')
print('You got ' + str((score / 4) * 100) + ' % .')