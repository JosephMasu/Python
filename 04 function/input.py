# input(): it's a function that prompts the user to enter data returns the entered data as a string


name = input('What is your name?: ')
age = input('How old are you?: ')

age = int(age)
age = age + 1

print(f'Hi ' + name)
print(f'You are {age} years old')