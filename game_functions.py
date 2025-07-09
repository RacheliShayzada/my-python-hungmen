def get_guess_from_user():
    """Ask the player to guess a letter and return it in lowercase."""
    guess = input("Guess a letter: ")
    return guess.lower()