import random
words3 = ["any", "lot", "fit"]
words4 = ["test", "kart", "coal"]
goalword = []
puzzle = []
guessed = []

#welcome
print("Welcome to Hangman ---");

#Select letter count for game
puzzlelength = int(input("Please pick a word length (3-4)"))

if(puzzlelength == 3):
    randy = random.randrange(0, 3)
    setuppuzzle = words3[randy]
    for i in setuppuzzle:
        goalword.append(i)
        puzzle.append("_")
elif(puzzlelength == 4):
    randy = random.randrange(0, 3)
    setuppuzzle = words4[randy]
    for i in setuppuzzle:
        goalword.append(i)
        puzzle.append("_")

print(goalword)
print("\n")
while True:
    print("Puzzle")
    print(puzzle)
    playerguess = input("Pick a Letter: ")
    guessed.append(playerguess)
    print("Guessed letters")
    print(guessed)
    print("\n")
    x = 0
    for i in goalword:
        if(playerguess == goalword[x]):
            puzzle[x] = playerguess;
        x = x + 1
    if(goalword == puzzle):
        print("you win!!!!!");
        break
            




