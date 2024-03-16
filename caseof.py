move = input("Enter Move (W, E, A, D): ")
position = 0
if move == 'W':
    position -= 10
elif move == 'E':
    position += 10
elif move == 'A':
    position -= 1
elif move == 'D':
    position += 1
else:
    print("Beep")

print("Position:", position)

percentage = int(input("Enter the exam score as a percentage: "))

if percentage >= 90:
    grade = 'A*'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
elif percentage >= 40:
    grade = 'E'
elif percentage >= 30:
    grade = 'F'
elif percentage >= 20:
    grade = 'G'
else:
    grade = 'U'

print("Your grade is:",grade)
