import random


def help_message():
    print("\nTo beat the computer you must guess if the next number is going to be higher or lower than the previous\n"
          "number displayed. If you guess correctly 3 times in a row before the computer you will win the game.\n"
          "Guessing incorrectly will reset your score so be careful!\n"
          "To make your choice, simply type 'higher' or 'lower' and then press enter. The next number will be created\n"
          "randomly between 0 and 100, so make your guess wisely. The game will then display your score and if the\n"
          "computer guessed correctly or incorrectly. If at any point you want to return to the application selection\n"
          "menu you can type 'quit'.")


def higher_lower():
    playing = True
    # main game loop, keeps the game going until the player inputs "quit"
    while playing:
        previous_number = random.randint(0, 100)
        player_score = 0
        computer_score = 0
        print("\nWelcome to the higher or lower game, to win you must correctly guess if the next number is going to be"
              "\nhigher or lower than the last number 3 times in a row. Your score will reset if you guess incorrectly."
              "\nNumbers will be created randomly between 0 and 100, so pick your answer wisely."
              "\nType 'quit' to go back to the main menu or 'help' if you are stuck.")
        # loops while the player and computer scores are less then 3 (nobody has won)
        while player_score < 3 and computer_score < 3:
            # loops to regenerate the next number if it is equal to the previous number
            while True:
                next_number = random.randint(0, 100)
                if next_number == previous_number:
                    continue
                else:
                    break
            player_choice = input(f"\nWill the next number be higher or lower than {previous_number}? ").lower().strip(" ")
            # logic for the computer to decide higher or lower
            if previous_number < 50:
                computer_choice = "higher"
            else:
                computer_choice = "lower"
            # check the player input and display a message or end the game appropriately
            if player_choice not in ["higher", "lower", "quit", "help"]:
                print("Please choose from higher or lower, type 'help' if you are stuck or 'quit' to end the game. ")
                continue
            elif player_choice == "quit":
                playing = False
                break
            elif player_choice == "help":
                help_message()
            else:
                print(f"The next number is: {next_number}")
                # logic to check if the computer was correct and sets the score accordingly
                if (computer_choice == "lower" and next_number < previous_number) or \
                        (computer_choice == "higher" and next_number > previous_number):
                    print(f"The computer guessed {computer_choice} correctly.")
                    computer_score += 1
                else:
                    print(f"The computer guessed '{computer_choice}' incorrectly!")
                    computer_score = 0
                # Logic to check if the player was correct and sets the score accordingly
                if (player_choice == "higher" and next_number > previous_number) or \
                        (player_choice == "lower" and next_number < previous_number):
                    print(f"You are correct!")
                    player_score += 1
                else:
                    print(f"Your guess was wrong :(")
                    player_score = 0
                print(f"The scores are: Computer {computer_score}, Player: {player_score}")
                previous_number = next_number
        else:
            # end of while loop : player and/or computer has guessed correctly 3 times in a row
            # logic to decide who has won or if it was a draw
            if player_score > computer_score:
                print("\nCongratulations, you are smarter then the computer!")
            elif player_score < computer_score:
                print("\nUnfortunately the computer beat you this time, you should try again!")
            else:
                print("\nIt was a draw! Maybe you'll win next time?")
