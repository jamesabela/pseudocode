"""
Token ← True
IF Token = True
 THEN
   OUTPUT "Entry Allowed"
ENDIF

"""

token = True

if token == True:
    print("Entry Allowed")

"""
height ← 99
IF height < 107
 THEN 
   OUTPUT "No Entry Allowed"
 ELSE 
   OUTPUT "Entry Allowed"
 ENDIF
"""
height = 99

if height < 107:
    print("No Entry Allowed")
else:
    print("Entry Allowed")

"""
"""

answer = 50
if answer < 0 or answer > 100:
    correct = False
else:
    correct = True
print(correct)



ChallengerScore = 72
ChampionScore = 82
HighestScore = 44
ChallengerName = "Mark"
Player1Name = "Player 1"
ChampionName = "James"

if ChallengerScore > ChampionScore:
    if ChallengerScore > HighestScore:
        print(ChallengerName, "is champion and highest scorer")
    else:
        print(Player1Name,"is the new champion")
else:
    if ChampionScore > HighestScore:
        print(ChampionName,"is still the champion and is also the highest scorer")
    else:
        print(ChampionName,"is still the champion")
