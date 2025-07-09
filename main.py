from consts import HANGMAN_ASCII_ART, MAX_TRIES
from game_functions import get_guess_from_user, create_display_word


def main():
    print(HANGMAN_ASCII_ART + str(MAX_TRIES))

    secret_word = input("Please enter a word: ")
    display = create_display_word(secret_word)
    print(display)
    
    guess = get_guess_from_user()
    print(guess)


if __name__ == "__main__":
    main()
