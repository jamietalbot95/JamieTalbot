import time

difficulty_one = ["My name is Jamie."]
difficulty_two = ["There was once a boy called Tim, his best friend was called Kim."]
difficulty_three = ["'Put your hands in the air!' The Policeman shouted at the top of his lungs. The robber might have had a knife (hidden in his trousers)"
                    " so the Policeman didn't want to take any risks."]


class Timer:
    def __init__(self,difficulty):
        self.difficulty = difficulty
        self.start_time = time.time()

    def time_taken(self):
        return round(time.time() - self.start_time,3)

    def is_quick_enough(self):
        if self.difficulty == 1:
            if time.time() - self.start_time < 10:
                return True
        if self.difficulty == 2:
            if time.time() - self.start_time < 20:
                return True
        if self.difficulty == 3:
            if time.time() - self.start_time < 40:
                return True


def typing_game_welcome_message():
    print("\nWelcome to the typing game. You will be asked to select your difficulty based on how confident you are at"
          "\ntyping. The game will then display a sentence which you will have to type within the allocated time frame."
          "\nWhen you have entered your attempt, the game will tell you if you were quick enough.\n")
    typing_game_main()



def typing_game_main():
    menu_open = True
    while menu_open:
        difficulty = input("\nThe following difficulties are available:"
                               "\n1. Level one (for your Grandma)\n"
                               "2. Level two (for the average Joe)\n"
                               "3. Level three (for keyboard ninjas)\n"
                               "\nThe following options are available:\n"
                               "4. Help - Displays a helpful message.\n"
                               "5. Quit - Returns to the applications main menu.\n"
                               "\nPlease select your option: ").strip(" ")
        if difficulty in ["1","2","3","4","5"]:
            difficulty = int(difficulty)
            if difficulty == 4:
                print("\nYou will be asked to select your difficulty based on how confident you are at"
                        "\ntyping. The game will then display a sentence which you will have to type within the allocated time frame."
                        "\nWhen you have entered your attempt, the game will tell you if you were quick enough.\n")
            elif difficulty == 5:
                menu_open = False
            else:
                question(difficulty)
        else:
            print(f"\n{difficulty} is not a valid input, choose from 1, 2, 3, 4 or 5.")


def time_allowed(difficulty):
    if difficulty == 1:
        return 10
    elif difficulty == 2:
        return 15
    elif difficulty == 3:
        return 30


def question(difficulty):
    sentence = ""
    print("\nType the below sentence as quickly as possible, pay attention to capitals and punctuation. "
          "\nPress enter when you have finished."
          "\nPress any key when you are ready to begin:")
    input()
    if difficulty == 1:
        print(difficulty_one[0])
        sentence = difficulty_one[0]
    elif difficulty == 2:
        print(difficulty_two[0])
        sentence = difficulty_two[0]
    elif difficulty == 3:
        print(difficulty_three[0])
        sentence = difficulty_three[0]
    typing_timer = Timer(difficulty)
    player_entry = input("\n")
    if typing_timer.is_quick_enough():
        if player_entry == sentence:
            print(f"\nGood job! You finished in {typing_timer.time_taken()} seconds")
        else:
            print("\nThat did not match the original sentence. You must have made a typo.")
    else:
        print(f"\nYou needed to complete the sentence in {time_allowed(difficulty)} seconds "
              f"it took you {typing_timer.time_taken()} seconds. Have another go!")

