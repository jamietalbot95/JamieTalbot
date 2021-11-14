import datetime
import high_lower_game
import school_timetable
import hangman
import calculator
import spelling_checker
import parts_of_speech
import typing_game

now = datetime.datetime.now()
hour = now.hour
valid_features = ["1", "2", "3", "4", "5", "6", "7", "help", "quit"]
playing = True


def welcome_message():
    if hour < 12:
        greeting = "\nGood morning, welcome to the School Helper Application."
    elif hour < 18:
        greeting = "\nGood afternoon, welcome to the School Helper Application."
    else:
        greeting = "\nGood evening, welcome to the School Helper Application."
    print("{}".format(greeting))


def run_selected_feature(feature):
    if feature == "1":
        calculator.calculator_main()
    elif feature == "2":
        school_timetable.school_timetable_main()
    elif feature == "3":
        spelling_checker.spelling_checker_main()
    elif feature == "4":
        high_lower_game.higher_lower()
    elif feature == "5":
        hangman.main_game()
    elif feature == "6":
        parts_of_speech.pof_game()
    elif feature == "7":
        typing_game.typing_game_welcome_message()


def main_menu():
    print("\nThe following features are available to use:\n"
          "1. Calculator\n"
          "2. School timetable\n"
          "3. Spelling checker\n"
          "4. Higher or lower game\n"
          "5. Hangman\n"
          "6. Verbs, Nouns and Adjectives\n"
          "7. Typing game")


while playing:
    welcome_message()
    main_menu()
    while True:
        feature_selection = input("\nPlease type the number of the feature you would like to use.\nType 'help' if you "
                                  "are unsure what to do or 'quit' to close the program: ").lower().strip(" ")
        if feature_selection in valid_features:
            if feature_selection == "quit":
                playing = False
                break
            elif feature_selection == "help":
                print("\nFrom the menu type the number of the application you would like to open and press enter. For example" 
                      "\nto open the calculator type '1' followed by enter. You will then be taken to the application"
                      "\nwhere further instructions will be available. If you want to close this program simply type"
                      "\n'quit'. The following features are available to use:\n"
                      "1. Calculator\n"
                      "2. School timetable\n"
                      "3. Spelling checker\n"
                      "4. Higher or lower game\n"
                      "5. Hangman\n"
                      "6. Verbs, Nouns and Adjectives\n"
                      "7. Typing game")
                continue
            run_selected_feature(feature_selection)
            break
        else:
            print("\nThe option you selected was not quite right, please try again.")
            continue