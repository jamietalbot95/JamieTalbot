import random
parts_of_speech = {"nouns":["sister","park"],"adjectives":["green"],"verbs":["jogged"]}
sentence = "My sister jogged around the green park."


def pof_game():
    playing = True
    while playing:
        print("\nWelcome to the verbs, nouns and adjectives game. You will be given a sentence which will contain\n"
              "verbs, nouns and adjectives. You will then be asked to identify and type either the verbs, the nouns or"
              "\nthe adjectives in the sentence. You can type 'help' if you are unsure what to do and\n"
              "'quit' to return to the applications main menu.")
        while True:
            start_game = input("\nAre you ready to begin? Type 'yes' , 'help' or 'quit': ").lower().strip(" ")
            if start_game not in ["yes","quit","help"]:
                print("Please choose from 'Yes', 'Help' or 'Quit'")
                continue
            elif start_game == "yes":
                pof_to_find = select_random_pof()
                print(f"\nSentence: {sentence}")
                print(f"\nPlease type all of the {pof_to_find} in the above sentence, separated by a comma.")
                student_input = input(f"{pof_to_find} = ").split(",")
                student_input.sort()
                parts_of_speech[pof_to_find].sort()
                if student_input == parts_of_speech[pof_to_find]:
                    print("Well done that is the correct answer!")
                else:
                    print(f"That was not quite right, the {pof_to_find} were {parts_of_speech[pof_to_find]}."
                          f"\nYou should try again!")
            elif start_game == "help":
                print("\nThe game will display a sentence, which contains nouns, verbs and adjectives. You will then be"
                      "\nasked to type all of the the nouns, verbs or adjectives that you can identify in the sentence."
                      "\nSeparate each word with a single comma. For example: flying,running. If you want to end the"
                      "\ngame simply type 'quit' when you are asked if you are ready to begin.")
            elif start_game == "quit":
                playing = False
                break


def select_random_pof():
    pof_to_find = random.choice(["nouns","verbs","adjectives"])
    return pof_to_find
