# Initialize the list with five empty strings
StudentNames = [""] * 5

# Assign names to each element
StudentNames[0] = "Ali"
StudentNames[1] = "Bruno"
StudentNames[2] = "Charlie"
StudentNames[3] = "Diana"
StudentNames[4] = "Ethan"

print(StudentNames[3])

"""
DECLARE NoughtsAndCrosses : ARRAY[1:3, 1:3] OF CHAR
NoughtsAndCrosses[2,3] ← ꞌXꞌ 
"""
# Initialize a 3x3 matrix
NoughtsAndCrosses = [[''] * 3 for _ in range(3)]  # Adjusted for 0-based indexing in Python

# Assign 'X' to the cell at (2, 3) considering 1-based indexing in pseudocode
NoughtsAndCrosses[1][2] = 'X'  # Adjusted for 0-based indexing in Python

print("NoughtsAndCrosses:")
for row in NoughtsAndCrosses:
    print(row)
