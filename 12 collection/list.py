# list[]: ordered and changeable, duplicate okay

languages = ['c', 'java', 'python', 'javascript']

print(languages[0])
# print(dir(languages))
# print(help(languages))

languages[3] = 'ruby'
for language in languages:
    print(language)

