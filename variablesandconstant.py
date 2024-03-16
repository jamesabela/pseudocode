"""
Example – variable declarations
DECLARE Counter : INTEGER
DECLARE TotalToPay : REAL
DECLARE GameOver : BOOLEAN

CONSTANT <identifier> ← <value>
CONSTANT HourlyRate ← 6.50

The assignment operator is ←
"""


Counter: int = 0
TotalToPay: float = 0
GameOver: bool = False
NumberOfHours: int = 0

HourlyRate = 6.50 # Constant, please don't change

NumberOfHours = 10
Counter = 0
Counter = Counter + 1
TotalToPay = NumberOfHours * HourlyRate
