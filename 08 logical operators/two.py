gpa = 2.0
attendance = True  
pass_status = 'Yes' if gpa >= 2.5 else 'No'
print(pass_status)
if gpa >= 4 or (2.5 <= gpa < 4 and attendance):
    print("Congratulations, you have passed!")
elif gpa < 2.5 and not attendance:
    print("Sorry, you have failed due to low GPA and poor attendance.")
else:
    print("Sorry, you have failed.")
