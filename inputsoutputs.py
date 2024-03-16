"""
Input and output (8.1.3)
Values are input using the INPUT command as follows:
    INPUT <identifier>
The identifier should be a variable (that may be an individual element of a data structure such as an array).
Values are output using the OUTPUT command as follows:
    OUTPUT <value(s)>
Several values, separated by commas, can be output using the same command.
Examples – INPUT and OUTPUT statements
INPUT Answer
OUTPUT Score
OUTPUT "You have ", Lives, " lives left"

"""

# DECLARE Answer : STRING
# OUPUT "Answer?"
# INPUT Answer
Answer = input("Answer?")

# DECLARE Num : INTEGER
# OUTPUT "Number?"
# INPUT Num

Num = int(input("Number?"))

# Score <-- 5000
# Lives <-- 3
# OUTPUT "This is some text"
# OUTPUT Score
# OUTPUT "You have ", Lives, " lives left"

Score = 5000
Lives = 3

print("This is some text")
print(Score)
print("You have",Lives,"lives left")
