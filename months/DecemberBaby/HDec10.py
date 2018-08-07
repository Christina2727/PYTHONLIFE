#Heather Loree
#Dec 10
#guessing_game_fun
""" We are making a game to ask the player to pick the right number"""


import random

computers_number = random.randint(1,100)
prompt = ' What is your guess? '

def do_guess_round():
    """ requesting a guess from the user, turning into a integer and giving a result
    of to high to low or correct"""
    computers_number = random.randint(1,100)
    while True:
        players_guess = int(input(prompt))
        if computers_number == int(players_guess):
            print('correct!')
            break
        elif computers_number > int (players_guess):
            print('Too low')
        else:
            print('Too high')

while True:
    #Print statment added
    print("Starting a new Round!")
    print("The computer's number should be "+str(computers_number))
    print("Let the guessing begin!!!")
    do_guess_round()
    print("") # blank line
 
