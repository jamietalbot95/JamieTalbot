phrase = "\nA structure which humans occupy?"
answer = "building"


def ask_question():
    print(phrase)
    student_answer = input("\nThe answer will only be one word. What is your answer? ").lower().strip(" ")
    if student_answer == answer:
        print(f"\nCongratulations that is correct! '{answer}' was the correct answer.")
    else:
        print(f"\nUnfortunately '{student_answer}' is the wrong answer, the correct answer is '{answer}'.")


def spelling_checker_main():
    checker_open = True
    while checker_open:
        print("\nWelcome to the spelling checker application. In this application you will be presented with a random\n"
              "phrase or question. You must complete the phrase or answer the question with correct spelling.\n"
              "The application will then tell you if your spelling was correct or incorrect and display the correct\n"
              "spelling. Type 'help' to display the help message or 'quit' to return to the application selection menu.")
        while True:
            player_choice = input("\nAre you ready to start learning? Choose from 'yes' , 'help' or 'quit': ").lower().strip(" ")
            if player_choice not in ["help","yes","y","no","n","quit"]:
                print("\nPlease enter a answer from: 'help' , 'yes' or 'quit'")
            elif player_choice == "help":
                print("\nThe computer will ask you a question, you should then type your answer to the question\n"
                      "paying close attention to spelling. The computer will then tell you if you were right or wrong.")
                continue
            elif player_choice in ["yes","y"]:
                print("\nAwesome! Lets get started. Here's your first question: ")
                ask_question()
                continue
            elif player_choice in ["no","n"]:
                print("\nWhy??? Learning is fun!")
                continue
            elif player_choice == "quit":
                checker_open = False
                break
