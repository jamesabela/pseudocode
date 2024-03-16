move = input("Enter Move (W, E, A, D): ")
position = 0  # Initialize position, you can set this to another value as needed

match move:
    case 'W':
        position -= 10
    case 'E':
        position += 10
    case 'A':
        position -= 1
    case 'D':
        position += 1
    case _:
        print("Beep")

print("Position:", position)

# Grades

percentage = 85
grade = ""
match percentage:
    case p if 90 <= p <= 100:
        grade =  'A*'
    case p if 80 <= p < 90:
        grade =  'A'
    case p if 70 <= p < 80:
        grade =  'B'
    case p if 60 <= p < 70:
        grade =  'C'
    case p if 50 <= p < 60:
        grade =  'D'
    case p if 40 <= p < 50:
        grade =  'E'
    case p if 30 <= p < 40:
        grade =  'F'
    case p if 20 <= p < 30:
        grade =  'G'
    case _:
        grade =  'U'

print("The grade for",percentage,"is", grade)
