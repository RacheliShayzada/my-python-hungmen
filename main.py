from consts import HANGMAN_ASCII_ART, MAX_TRIES
from game_functions import get_guess_from_user


def main():
    print(HANGMAN_ASCII_ART + str(MAX_TRIES))
    
    guess = get_guess_from_user()
    print(guess)


if __name__ == "__main__":
    main()
