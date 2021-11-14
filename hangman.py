import random
import string


def show_status(hidden_word, lives, guesses):
    print(f"\nYour current guesses are: {guesses}")
    if lives == 1:
        print(f"\nYou have {lives} life remaining.")
    else:
        print(f"\nYou have {lives} lives remaining.")
    print("\n","".join(hidden_word))


def ask_for_guess():
    guessed_letter = input("\nPlease enter your next guess: ").lower().strip(" ")
    return guessed_letter


def pick_random_word():
    file = open("word_list.txt")
    words = file.readlines()
    word = random.choice(words)
    word = str(word).strip("\n")
    file.close()
    return word


def hide_word(word):
    hidden_word = []
    for letters in word:
        hidden_word.append("*")
    return hidden_word


def check_if_guessed(guessed_letter,guesses):
    return guessed_letter in guesses


def correct_guess(guessed_letter, guesses, word, hidden_word):
    guesses += guessed_letter
    for letters in range(0, len(word)):
        if word[letters] == guessed_letter:
            hidden_word[letters] = guessed_letter
    return hidden_word, guesses


def check_if_winner(word, hidden_word):
    return word == "".join(hidden_word)


def main_game():
    play_again = True
    print("\nWelcome to hangman, the rules are simple, you have 8 lives to guess letters until the hidden word is"
          " revealed.\nYou will lose a life if your guess is wrong. You can type 'help' if you are unsure what to\ndo"
          " and 'quit' if you want to go back to the main menu.")
    while play_again:
        guesses = ""
        lives = 8
        word = pick_random_word()
        hidden_word = hide_word(word)
        while True:
            start_game = input("\nAre you ready to play? Type 'yes' to begin.\nOr type 'help' if you are unsure what to do and 'quit' to go back to the main menu: ").lower().strip(" ")
            if start_game in ["help","quit","yes"]:
                if start_game == "help":
                    print("\nPlease type yes when asked if you want to begin the game. Once the game starts you will be\n"
                          "presented with a 5 character word, hidden by *'s, you will have 8 guesses to unveil the\n"
                          "word. You cannot guess the same letter twice. A correct guess will replace the *'s with\n"
                          "the guess.")
                elif start_game == "yes" or start_game == "quit":
                    break
            else:
                print("Please choose from the following options: 'yes' to start the game, 'help' if you are unsure what to do or 'quit' to go back to the main menu")
        if start_game == "yes":
            while lives > 0:
                show_status(hidden_word, lives, guesses)
                guessed_letter = ask_for_guess()
                if len(guessed_letter) > 1 or len(guessed_letter) == 0:
                    print("Please only guess a single letter at a time.")
                elif check_if_guessed(guessed_letter, guesses):
                    print("\nYou already guessed that letter.")
                elif guessed_letter not in string.ascii_lowercase:
                    print("Please only guess characters from the alphabet.")
                else:
                    if guessed_letter in word:
                        hidden_word, guesses = correct_guess(guessed_letter, guesses, word, hidden_word)
                        if check_if_winner(word,hidden_word):
                            print(f"\nCongratulations you win! The word is {word}.")
                            break
                    else:
                        print("\nSadly, that guess was incorrect, keep trying though!")
                        lives -= 1
                        guesses += guessed_letter
            else:
                print(f"\nOh dear, you lost this game :( You should definitely try again! The word was {word}.")
        elif start_game == "quit":
            play_again = False