
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
            break