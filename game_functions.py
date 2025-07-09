def get_guess_from_user():
    """
    Asks the user to guess a letter.
    Keeps asking until the user provides a valid single English letter.
    Returns the valid lowercase letter.
    """
    while True:
        user_input = input("Guess a letter: ").strip()

        # Empty input
        if user_input == "":
            print("❌ You must enter a letter!")
            continue

        # Case 1: both multiple characters and invalid characters
        if len(user_input) > 1 and (not user_input.isalpha() or not user_input.isascii()):
            print("❌ Error: Please enter only ONE English letter (a-z or A-Z).")
            continue

        # Case 2: more than one character
        if len(user_input) > 1:
            print("❌ Error: Only ONE letter allowed.")
            continue

        # Case 3: not a valid English letter
        if not user_input.isalpha() or not user_input.isascii():
            print("❌ Error: Only English letters are allowed (a-z or A-Z).")
            continue

        # Valid input
        return user_input.lower()


def create_display_word(secret_word):
    """
    Receives the secret word and returns a string with underscores 
    representing each letter in the word, separated by spaces.
    Example: 'hangman' → '_ _ _ _ _ _ _'
    """
    return " ".join(["_"] * len(secret_word))
