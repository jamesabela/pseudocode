"""
DECLARE highScore: INTEGER

FUNCTION ReadHighScoreFromFile() RETURNS INTEGER
    DECLARE score AS INTEGER
    OPENFILE "highscore.txt" FOR READ
        READFILE "highscore.txt", score
    CLOSEFILE "highscore.txt"
    IF score = ""
    THEN
       RETURN 0
    ELSE
       RETURN score
END FUNCTION


PROCEDURE SaveHighScoreToFile(score: INTEGER)
    OPENFILE "highscore.txt" FOR WRITE
    WRITEFILE "highscore.txt", score
    CLOSEFILE "highscore.txt"
ENDPROCEDURE

DECLARE currentScore AS INTEGER
highScore ← ReadHighScoreFromFile()
INPUT currentScore

IF currentScore > highScore THEN
    CALL SaveHighScoreToFile(currentScore)
ENDIF


"""
def read_high_score_from_file():
    try:
        with open("highscore.txt", "r") as file:
            score = file.read()
            return int(score) if score else 0
    except FileNotFoundError:
        return 0

def save_high_score_to_file(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))

# Assume this function is part of the game that retrieves the current game score
def get_score_from_game():
    # Placeholder for actual game score retrieval
    return int(input("Enter the current game score: "))

high_score = read_high_score_from_file()
current_score = get_score_from_game()

if current_score > high_score:
    save_high_score_to_file(current_score)
    print(f"New high score saved: {current_score}")
else:
    print(f"High score remains: {high_score}")
