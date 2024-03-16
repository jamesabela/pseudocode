"""
PROCEDURE HorizontalRule
    OUTPUT "----------------------------"
ENDPROCEDURE

CALL HorizontalRule()
"""

def DefaultLine():
    print("----------------------------")

DefaultLine()

"""
PROCEDURE Line(Size : INTEGER)
    DECLARE Length : INTEGER
    FOR Length ← 1 TO Size
        OUTPUT '-'
    NEXT Length
ENDPROCEDURE

CALL Line(MySize)

"""

def Line(Size: int):
    for Length in range(0,Size):
        print("-",end="")

Line(10)
