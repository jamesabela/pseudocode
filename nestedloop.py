"""
Total ← 0
FOR Row ← 1 TO MaxRow
    RowTotal ← 0
    FOR Column ← 1 TO 10
        RowTotal ← RowTotal + Amount[Row, Column]
    NEXT Column
    OUTPUT "Total for Row ", Row, " is ", RowTotal
    Total ← Total + RowTotal
NEXT Row
OUTPUT "The grand total is ", Total
"""
import random

# Assuming MaxRow and Amount are defined
MaxRow = 5  # Example value
Amount = [[random.randint(1, 100) for _ in range(10)] for _ in range(MaxRow)]  # Generating a 2D list of random numbers

Total = 0

for Row in range(MaxRow):  # Python's range starts at 0 by default
    RowTotal = 0
    for Column in range(10):  # Iterating through 10 columns
        RowTotal += Amount[Row][Column]
    print("Total for Row",Row + 1,"is",RowTotal)  # Adding 1 to Row for display since Python is 0-indexed
    Total += RowTotal

print("The grand total is",Total)

