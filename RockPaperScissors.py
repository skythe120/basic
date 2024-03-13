import random
wins = 0
pwin = 0
cwin = 0
def PlayerSelect():
    Pchk = 0;
    
    while(Pchk < 1):
        GetPChoice = input("[R]ock - [P]apper - [S]cissors! ");
        if(GetPChoice == "R" or GetPChoice == "ROCK" or GetPChoice == "rock" or GetPChoice == "r"):
            GetPChoice = "Rock"
            Pchk = 1;
        elif(GetPChoice == "P" or GetPChoice == "PAPER" or GetPChoice == "paper" or GetPChoice == "p"):
            GetPChoice = "Paper"
            Pchk = 1;
        elif(GetPChoice == "S" or GetPChoice == "SCISSORS" or GetPChoice == "scissors" or GetPChoice == "s"):
            GetPChoice = "Scissors"
            Pchk = 1;
        else:
            GetPChoice = "invalid";
            print("Invalid Choice");
        
    return GetPChoice;


def ComputerSelect():
    ComputerOptions = ["Rock", "Paper", "Scissors"]
    ComputerChoice = random.choice(ComputerOptions)
    return ComputerChoice

while(wins < 3):
    PlayerSelectFinal = PlayerSelect(); 
    ComputerSelectFinal = ComputerSelect();
    if(PlayerSelectFinal == "Rock" and ComputerSelectFinal == "Paper"):
        print(f"Player Selected: {PlayerSelectFinal} and Computer Selected {ComputerSelectFinal}")
        print("Computer Wins round");
        wins = wins + 1
        cwin = cwin + 1
    elif (PlayerSelectFinal == "Paper" and ComputerSelectFinal == "Scissors"):
        print(f"Player Selected: {PlayerSelectFinal} and Computer Selected {ComputerSelectFinal}")
        print("Computer Wins round");
        wins = wins + 1
        cwin = cwin + 1
    elif (PlayerSelectFinal == "Scissors" and ComputerSelectFinal == "Rock"):
        print(f"Player Selected: {PlayerSelectFinal} and Computer Selected {ComputerSelectFinal}")
        print("Computer Wins round");
        wins = wins + 1
        cwin = cwin + 1
    elif (PlayerSelectFinal == ComputerSelectFinal):
        print(f"Player Selected: {PlayerSelectFinal} and Computer Selected {ComputerSelectFinal}")
        print("Tied Round");
    else:
        print(f"Player Selected: {PlayerSelectFinal} and Computer Selected {ComputerSelectFinal}")
        print("Player Wins round");
        wins = wins + 1
        pwin = pwin + 1


if(pwin > cwin):
    print(f"Player wins the game {pwin} to {cwin}")
else:
    print(f"Computer wins the game {cwin} to {pwin}")
 
