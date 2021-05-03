marks = input('Please your marks: ')
marks = float(marks)

if marks >= 80:
    grade = "A+"
    print('Your grade is' , grade)
    input('Congrats! You got a letter mark!')
elif marks >= 70:
    grade = "A"
    print('Your grade is' , grade)
elif marks >= 60:
    grade = 'A-'
    print('Your grade is' , grade)
elif marks >= 50:
    grade = 'B'
    print('Your grade is' , grade)
else:
    grade = 'F'
    print('Your grade is' , grade)
    input('You have failed')
