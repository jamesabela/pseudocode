"""
DECLARE StudentNames : ARRAY[1:30] OF INTEGER
//assume these have values

PROCEDURE BubbleSort(Arr)
    DECLARE n AS INTEGER
    DECLARE swapped AS BOOLEAN
    n ← LENGTH(Arr)
    REPEAT
        swapped ← FALSE
        FOR i ← 1 TO n-1
            IF Arr[i] > Arr[i + 1] THEN
                SWAP(Arr[i], Arr[i + 1])
                swapped ← TRUE
            ENDIF
        NEXT i
        n ← n - 1
    UNTIL NOT swapped
ENDPROCEDURE

"""

import random
def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:  # Adjusted for zero-based indexing
                arr[i - 1], arr[i] = arr[i], arr[i - 1]  # Swap elements
                swapped = True
        n -= 1

# Initialize the list with integers
StudentNames = [random.randint(1, 100) for _ in range(30)]  # Example: generate a list of 30 random integers

print("Original list:", StudentNames)
bubble_sort(StudentNames)
print("Sorted list:", StudentNames)
