import random

def rollDice():
    rolls = []
    for roll in range(6):
        rolls.append(random.randint(1,6))
    return rolls