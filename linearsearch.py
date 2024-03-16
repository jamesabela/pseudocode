"""
DECLARE numbers : ARRAY[1:30] OF INTEGER
DECLARE target AS INTEGER
DECLARE found AS BOOLEAN
SET found TO FALSE

FOR number 1 <-- to 30
    IF numbers[number] = target 
  THEN
        SET found TO TRUE
        OUTPUT "Target found.
    ENDIF
NEXT

IF NOT found THEN
    OUTPUT "Target not found."
ENDIF

"""
import random

numbers = [random.randint(1, 100) for _ in range(30)]
target = int(input("Enter the target number: "))
found = False

for number in numbers:
    if number == target:
        found = True
        print("Target found.")
        break  # Exit the loop once the target is found

if not found:
    print("Target not found.")
