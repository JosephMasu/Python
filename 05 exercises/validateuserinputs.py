username = input('Enter your name: ')

if len(username) > 12:
    print('Your user name can not be more than 12 chracters.')
elif not username.find(' ') == -1:
    print('Your username can not contain spaces')
elif not username.isdigit():
    print('Your username can not usernam')
else:    
    print(f'Hello {username}')