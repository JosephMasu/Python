operator = input('Choose an operator: (+ - * /)')

number_1 = int(input('Enter first number: '))
number_2 = int(input('Enter second number: '))

if operator == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)
elif operator == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)
elif operator == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)
elif operator == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)
else:
    print(f'{operator} is not a valid operator.')
