# if statement 

age = int(input("Enter your age: "))

if age >= 16:
    print('You are old enough to drive')

elif age < 0:
    print('you are not yet born')
else:
    print('You are not old enough to drive')