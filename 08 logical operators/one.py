# or logical operator at least one condition should be true

gpa = 4.5
student_passed = True

if gpa >= 4 or gpa <= 2.4 or student_passed:
    print('congratulations you have passed')
else:
    print('sorry you have failed')


# and logical operator both condition conditions must be true

if gpa >= 2.5 and student_passed:
    print('congratulations you have passed')
else:
    print('sorry you have failed')

