"""
DECLARE board AS ARRAY[1:3, 1:3] OF CHAR
DECLARE currentPlayer AS CHAR
DECLARE winner AS CHAR
DECLARE moveCount AS INTEGER

PROCEDURE InitializeBoard()
    FOR row FROM 1 TO 3
        FOR column FROM 1 TO 3
            board[row, column] ← ' '
        NEXT column
    NEXT row
    moveCount ← 0
    currentPlayer ← 'X'
    winner ← ' '
END PROCEDURE

PROCEDURE PrintBoard()
    FOR row FROM 1 TO 3
        OUTPUT board[row, 1] + '|' + board[row, 2] + '|' + board[row, 3]
        IF row < 3 THEN
            OUTPUT "-----"
        ENDIF
    NEXT row
END PROCEDURE

FUNCTION CheckWinner() AS CHAR
    FOR row FROM 1 TO 3
        IF board[row, 1] = board[row, 2] AND board[row, 2] = board[row, 3] AND board[row, 1] ≠ ' '
            RETURN board[row, 1]
        ENDIF
    NEXT row

    FOR column FROM 1 TO 3
        IF board[1, column] = board[2, column] AND board[2, column] = board[3, column] AND board[1, column] ≠ ' '
            RETURN board[1, column]
        ENDIF
    NEXT column

    IF board[1, 1] = board[2, 2] AND board[2, 2] = board[3, 3] AND board[1, 1] ≠ ' '
        RETURN board[1, 1]
    ENDIF

    IF board[1, 3] = board[2, 2] AND board[2, 2] = board[3, 1] AND board[1, 3] ≠ ' '
        RETURN board[1, 3]
    ENDIF

    RETURN ' '
END FUNCTION

PROCEDURE SwitchPlayer()
    IF currentPlayer = 'X' THEN
        currentPlayer ← 'O'
    ELSE
        currentPlayer ← 'X'
    ENDIF
END PROCEDURE

PROCEDURE MakeMove(row, column)
    IF board[row, column] = ' ' THEN
        board[row, column] ← currentPlayer
        moveCount ← moveCount + 1
    ELSE
        OUTPUT "Position already taken. Try again."
    ENDIF
END PROCEDURE

PROCEDURE GameLoop()
    InitializeBoard()
    WHILE winner = ' ' AND moveCount < 9
        PrintBoard()
        OUTPUT currentPlayer + "'s turn. Enter row and column: "
        INPUT row, column
        MakeMove(row, column)
        winner ← CheckWinner()
        IF winner = ' ' THEN
            SwitchPlayer()
        ENDIF
    END WHILE
    PrintBoard()
    IF winner ≠ ' ' THEN
        OUTPUT winner + " wins!"
    ELSE
        OUTPUT "It's a draw!"
    ENDIF
END PROCEDURE

CALL GameLoop
"""

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print("-----")

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def switch_player(current_player):
    return 'O' if current_player == 'X' else 'X'

def make_move(board, row, column, player):
    if board[row][column] == ' ':
        board[row][column] = player
    else:
        print("Position already taken. Try again.")

def game_loop():
    board = initialize_board()
    current_player = 'X'
    winner = None
    move_count = 0

    while winner is None and move_count < 9:
        print_board(board)
        row = int(input(f"{current_player}'s turn. Enter row: ")) - 1
        column = int(input("Enter column: ")) - 1
        make_move(board, row, column, current_player)
        winner = check_winner(board)
        if winner is None:
            current_player = switch_player(current_player)
        move_count += 1

    print_board(board)
    if winner:
        print(f"{winner} wins!")
    else:
        print("It's a draw!")

game_loop()
