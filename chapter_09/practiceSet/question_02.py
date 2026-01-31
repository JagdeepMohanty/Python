#The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score

def game():
    return int(input("Enter your score: "))

score = game()

with open("Hi-score.txt", "r") as f:
    hi_score = f.read()

if hi_score == "" or score > int(hi_score):
    with open("Hi-score.txt", "w") as f:
        f.write(str(score))
