grade = int(input("Please enter your grade: "))

if 0 <= grade <= 69:
    equivalent = 5.00
elif 70 <= grade <= 73:
    equivalent = 3.00
elif 74 <= grade <= 77:
    equivalent = 2.75
elif 78 <= grade <= 80:
    equivalent = 2.50
elif 81 <= grade <= 83:
    equivalent = 2.25
elif 84 <= grade <= 87:
    equivalent = 2.00
elif 88 <= grade <= 90:
    equivalent = 1.75
elif 91 <= grade <= 93:
    equivalent = 1.50
elif 94 <= grade <= 97:
    equivalent = 1.25
elif 98 <= grade <= 100:
    equivalent = 1.00

equivalent = round(equivalent, 2)
print(f'Your equivalent grade is {equivalent}')
