unit = input('Is this temperature in celsuis or fahrenheit?: (C/F)')
temp = float(input('What is the temperature?: '))

if unit == 'C':
    temp = round((9 * temp) / 5 + 32, 2)
elif unit == 'F':
    temp = round((temp - 32) * 5 / 9, 2)
else:
    print(f'{unit} is inalid.')
print(f'The temperature in {unit} is {temp}')