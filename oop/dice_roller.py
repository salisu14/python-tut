#!/usr/bin/env python3
from dice import Dice, Die

def main():
    print("The Dice Roller program")
    print()

    # get the number of dice from user
    count = int(input('Enter the number of dice to roll: '))

    # create Dice object and add Die objects to it
    dice = Dice()
    for i in range(count):
        die = Die()
        dice.addDie(die)
    
    while True:
        # roll the dice
        dice.rollAll()
        print("YOUR ROLL: ", end="")
        for die in dice.list:
            print(die.value, end=" ")
        print("\n")

        choice = input("Roll again? (y/n): ").lower()
        if choice != 'y':
            print("Bye!")
            break

if __name__ == '__main__':
    main()