#!/usr/bin/env python3

#Rock Paper Scissors game of chance


import random

While True:
    #This line will take input from the user
    player = input("Enter a number (1 for rock, 2 for paper, 3 for scissors) >>")
    RPS = [1,2,3]
    # Computer will randomly play number [1,3]
    computer = random.choice(RPS)
    # Show what computer played ("The computer played____")
    RPS_dict = {1:'Rock', 2:'Paper', 3:'Scissors'}
    print("The computer played", RPS_dict.get(computer))
    #The below lines for the random inputs from computer compared to the user and how results would happen
    def game(player, computer):
        if player == computer:
            print("Tie!")
        elif player == 1:
            if computer == 2:
                print("Computer won!", RPS_dict.get(computer), 'covers', RPS_dict.get(player))
            else:
                print("You win!", RPS_dict.get(player), "cut", RPS_dict.get(computer))

        elif player == 2
