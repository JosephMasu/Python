print('Welcome to the adventure game!')

answer = input('You are born today, choose your gender, boy or girl: ').lower()

if answer == 'girl':
    answer = input('You are a girl, do you want to be a queen or a princess? ').lower()
    if answer == 'queen':
        print('You will be a queen one day. You will have to work hard to rule your kingdom and be a good leader.')
    elif answer == 'princess':
        print('You will be a princess. You will have to learn how to be a good daughter, sister, and friend.')
    else:
        print('Invalid choice. Please restart the game and choose a valid option.')

elif answer == 'boy':
    answer = input('You are a boy, do you want to be a civilian or join the military? ').lower()
    if answer == 'civilian':
        print('You chose to be a civilian. You will live a peaceful life, contributing to society in your own way.')
    elif answer == 'military':
        answer = input('You joined the military. Do you want to work in the office or on the frontline? ').lower()
        if answer == 'office':
            print('You chose to work in the office. You will support the military operations from behind the scenes.')
        elif answer == 'frontline':
            print('You chose to be on the frontline. You will face challenges and dangers, but you will be remembered as a hero.')
        else:
            print('Invalid choice. Please restart the game and choose a valid option.')
    else:
        print('Invalid choice. Please restart the game and choose a valid option.')

else:
    print('Invalid gender. Please restart the game and choose a valid gender.')