#!/usr/bin/env python3
import random 

OPTIONS = ['rock', 'paper', 'scissors']

class RockPaperScissorsSimulator:
    def __init__(self):
        self.computer_choice = None
        self.human_choice = None
    
    def get_computer_choice(self):
        random.shuffle(OPTIONS)
        self.computer_choice = random.choice(OPTIONS)
       
    
    def get_human_choice(self):
        choice_number = int(input('Enter the number of your choice: '))
        self.human_choice = OPTIONS[choice_number - 1]
    
    def print_options(self):
        print('\n'.join(f'({i + 1}) {option.title()}' for i, option in enumerate(OPTIONS)))
    
    def print_choices(self):
        print(f'You choose {self.human_choice}')
        print(f'The computer chose {self.computer_choice}')
    
    def print_win_lose(self, human_beats, human_loses_to):
        if self.computer_choice == human_loses_to:
            print(f'Sorry, {self.computer_choice} beats {self.human_choice}')
        elif self.computer_choice == human_beats:
            print(f'Yes, {self.human_choice} beats {self.computer_choice}!')
    
    def print_result(self):
        if self.human_choice == self.computer_choice:
            print('Draw')
        
        if self.human_choice == 'rock':
            self.print_win_lose('scissors', 'paper')
        elif self.human_choice == 'paper':
            self.print_win_lose('rock', 'scissors')
        elif self.human_choice == 'scissors':
            self.print_win_lose('paper', 'rock')
    
    def simulate(self):
        self.print_options()
        self.get_human_choice()
        self.get_computer_choice()
        self.print_choices()
        self.print_result()

def main():

    ans = 'y'
    while ans == 'y':
        RPS = RockPaperScissorsSimulator()
        RPS.simulate()
        print()

        ans = input('Do you wish to play again? (y/n): ').lower()
        if ans == 'y':
            continue

if __name__ == '__main__': 
    main()