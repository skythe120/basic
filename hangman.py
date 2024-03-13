import random
playerguess = " ";
puzzlelength = 0
words3 = ["any", "lot", "fit"]
words4 = ["test", "kart", "coal"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
goalword = []
puzzle = []
guessed = []

def lettercheck(playerguess):
    accepted = 0
    while(accepted < 1):
        if(playerguess in letters):
            guessed.append(playerguess)
            accepted = 1
        else:
            print("Sorry that wasnt an acceptable letter")
            print("make sure you only guess one letter at a time and letters should be lowercase\n")
            playerguess = input("Pick a Letter: ")
    return playerguess
       

#welcome
print("Welcome to Hangman ---");

#Select letter count for game
while(puzzlelength < 3):
    puzzlelength = input("Please pick a word length (3-4)")
    try:
        puzzlelength = int(puzzlelength)
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
        else:
            print("Invalid option")
            puzzlelength = 0
    except ValueError:
        print("invalid entry")
        puzzlelength = 0
        

print("\n")
tries = 7
while True:
    print("Puzzle: ")
    print(puzzle)
    playerguess = input("Pick a Letter: ")
    playerguess = lettercheck(playerguess)
    print("Guessed letters")
    print(guessed)
    print("\n")
    x = 0
    for i in goalword:
        if(playerguess == goalword[x]):
            puzzle[x] = playerguess;
        x = x + 1
    if(goalword == puzzle):
        print (goalword)
        print("you win!!!!!");
        break
            
