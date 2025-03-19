username = input('Enter your name: ')

if len(username) > 12 and not username.find(' ') == -1 and not username.isdigit():
    print('Your user name can not be more than 12 chracters and can not contain spaces or digits')
else:
    print(f'Your name is {username}')