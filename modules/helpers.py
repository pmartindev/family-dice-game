import random

DICE_SET_SIZE = 5

def rollDice(rolls = []):
    numRolls = DICE_SET_SIZE - int(len(rolls))
    for roll in range(numRolls):
        rolls.append(random.randint(1,6))
    return rolls

def checkScore(diceSet):
    if len(diceSet) < DICE_SET_SIZE:
        print("Invalid array. Length is not large enough.")
        exit(1)

    sorted(diceSet, reverse = True)

    stash = []
    score = 0

    for dice in diceSet: 
        if dice not in stash and (dice == 6 or dice == 5 or dice == 4):
            stash.append(dice)
        else:
            score += dice
        
    if len(stash) < 3:
        return 0
    else:
        return score
    


