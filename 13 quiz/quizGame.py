# quiz game 

questions = ('what is 1 + 0 ?: ',
             'what is 1 + 1 ?: ',
             'what is 1 + 2 ?: ',
             'what is 1 + 3 ?: ',
             'what is 1 + 4 ?: ')

options = (('A. 1', 'B. 2', 'C. 3', 'D. 4', 'E. 5'),
           ('A. 1', 'B. 2', 'C. 3', 'D. 4', 'E. 5'),
           ('A. 1', 'B. 2', 'C. 3', 'D. 4', 'E. 5'),
           ('A. 1', 'B. 2', 'C. 3', 'D. 4', 'E. 5'),
           ('A. 1', 'B. 2', 'C. 3', 'D. 4', 'E. 5'),)

answers = ('A', 'B', 'C', 'D', 'E')

guesses = []
score = 0
question_num = 0

for question in questions:
    print('----------------------')
    print(question)
    for option in options[question_num]:
        print(option)   
    
    guess = input('Enter (A, B, C, D, E): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('CORRECT!')
    else:
        print('INCORRECT!')
        print(f'{answers[question_num]} is the correct answer')
    question_num += 1

print('----------------------')
print('       RESULTS        ')
print('----------------------')

print('answers: ', end='')
for answer in answers:
    print(answer, end=' ')
print()

print('guesses: ', end='')
for guess in guesses:
    print(guess, end=' ')
print()

score = int(score / len(questions) * 100)
print(f'Your score is: {score}%')



