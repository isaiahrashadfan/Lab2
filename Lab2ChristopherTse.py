# Lab 2
# Author: Christopher Tse
# Date: 19 February 2024

import random

# Guessing Game

def guessing_game():
    rnum = random.randint(1,100)
    tries = 5
    print("I'm thinking of a number between 1 and 100.")
    guess = int(input('Guess what it is. You have 5 tries: '))
    
    while (guess != rnum):
        tries -= 1
        if (tries > 0):
            guess = int(input('Nope! Too low. Try again (' + str(tries) + ' tries left): '))
        else:
            print('Nope! You lost. The number was ' + str(rnum))
            break
        if (guess == rnum):
            print('You got it!')
            break
        
    replay = str(input('Do you want to play again? (Y/N): '))
    if (replay == 'Y'):
        guessing_game()