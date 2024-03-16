"""
FUNCTION SumSquare(Number1:INTEGER, Number2:INTEGER) RETURNS INTEGER
    RETURN Number1 * Number1 + Number2 * Number2
ENDFUNCTION
sumofsquares <-- SumSquare(10, 20)
OUTPUT "Sum of squares = ",sumofsquares


"""
def SumSquare(Number1: int, Number2: int) -> int:
    return Number1 * Number1 + Number2 * Number2

sumofsquares = SumSquare(10, 20)
print(sumofsquares)
