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
    else:
        selection()


# Rock-Paper-Scissors
        
def rps():
    rnum = random.randint(1,3)
    inp = str(input('Do you want to play? (Y/N): '))
    if (inp == 'Y'):
        choice = int(input('Enter your choice:\t 1. paper\t2. scissors\t3. rock: '))
        if (rnum == 1):
            if (choice == 2):
                print('You won!')
            elif (choice == 3):
                print('You lost!')
            else:
                print("It's a tie!")
        if (rnum == 2):
            if (choice == 3):
                print('You won!')
            elif (choice == 1):
                print('You lost!')
            else:
                print("It's a tie!")
        if (rnum == 3):
            if (choice == 1):
                print('You won!')
            elif (choice == 2):
                print('You lost!')
            else:
                print("It's a tie!")
        rps()
    else:
        selection()

def selection():
    game = int(input('Which game do you want to play? \t1. Guessing Game\t2. Rock-Paper-Scissors\t3. Exit: '))
    if(game == 1):
        guessing_game()
    elif(game == 2):
        rps()
    else:
        print('Exiting...')

# Main
        
if __name__== "__main__":
    selection()