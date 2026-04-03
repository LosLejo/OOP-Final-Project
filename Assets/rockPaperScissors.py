import random

options = (1, 2, 3)

def randomChoice(conmputer):
    cchoice = 0
    
    computer = random.choice(options)
    
    if computer == 1:
        cchoice = 1
        return cchoice
    if computer == 2:
        cchoice = 2
        return cchoice
    if computer == 3:
        cchoice = 3
        return cchoice

def whoWin(user, computer):
    if user == computer:
        return 1
    elif user == 1 and computer == 3:
        return 2
    elif user == 2 and computer == 1:
        return 2
    elif user == 3 and computer == 2:
        return 2
    else:
        return 3
