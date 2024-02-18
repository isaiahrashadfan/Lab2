import random

def guessing_game():
    number = random.randint(1, 100)
    guess = 0
    attempts = 0

    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = random.choice(choices)

        if player_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        print(f"Computer chose {computer_choice}.")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    while True:
        print("Which game do you want to play?")
        print("1. Guessing Game")
        print("2. Rock-paper-scissors")
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            guessing_game()
        elif choice == "2":
            rock_paper_scissors()
        else:
            print("Invalid choice. Please enter 1 or 2.")

        play_again = input("Do you want to play another game? (yes/no): ").lower()
        if play_again != "yes":
            