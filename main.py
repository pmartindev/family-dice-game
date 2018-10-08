from modules import helpers
def main():
    diceSet = helpers.rollDice([6,5,4])

    print(diceSet)
    print(helpers.checkScore(diceSet))

if __name__ == "__main__":
    main()

