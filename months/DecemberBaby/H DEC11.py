#Heather Loree
#DEC 11
#Guessing_game_fun2

""" We are making a game to ask the player to pick the right number"""


import random


prompt = ' What is your guess? '

#new constants
QUIT = -1
QUIT_TEXT = 'q'
QUIT_MESSAGE = "Thank you for playing"
CONFIRM_QUIT_MESSAGE = 'are you sure you want to quit (y/n)? '




def confirm_quit():
    """ask user to confirm that they want to quit
    default to yes
    return true (yes, i want to quit) or false (no,dont quit)"""
    spam = input(CONFIRM_QUIT_MESSAGE)
    if spam == 'n':
        return False
    else:
        return True


def do_guess_round():
    """requesting a guess from the user, turning into a integer and giving a result
    of to high to low or correct"""
    computers_number = random.randint(1,100)
    number_of_guesses = 0 # Added
    while True:
        players_guess = (input(prompt))
        if players_guess == QUIT_TEXT:
            if confirm_quit():
                return QUIT
            else:
                continue # that is, do next round of loop

        number_of_guesses = number_of_guesses+1 # added
        if computers_number == int(players_guess):
            print('correct!')
            return number_of_guesses # changed
        elif computers_number > int (players_guess):
            print('Too low')
        else:
            print('Too high')

total_rounds = 0 # Added
total_guesses = 0 # Added

while True:
    total_rounds = total_rounds+1
    print("Starting Round number: " +str(total_rounds)) # changed
    print("Let the guessing begin!!!")
    this_round = do_guess_round()

    if this_round == QUIT:
        total_rounds = total_rounds -1
        avg = str(total_guesses/float(total_rounds))
        if total_rounds == 0:
            stats_message = 'you completed no rounds. '+\
                            'please try again later.'
        else:
            stats_message = 'you played ' + str(total_rounds) +\
                            ' rounds, with an average of '+\
                            str(avg)
            break

    
    total_guesses = total_guesses+this_round
    
    avg = str(total_guesses/float(total_rounds))
    print("you took "+str(this_round)+" guesses")
    print("your guessing average = "+str(avg))
    print("") # blank line

print(stats_message)
print(QUIT_MESSAGE)
 

