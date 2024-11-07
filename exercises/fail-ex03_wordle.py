"""ex03 - wordle- a word guessing game"""

__author__ = "730753182"


def input_guess(secret_word_len: int) -> str:
    """asks the user to input a word of a specified length"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input((f"That wasn't {secret_word_len} chars! Try again: "))
    else:
        return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """checks a word to see if it contains a character"""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if char_guess == secret_word[index]:
            return True
        else:
            index += 1
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """DOCSTRING"""
    assert len(user_guess) == len(secret_word)
    # emoji codes
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # initializations
    guess_index: int = 0
    secret_index: int = 0
    return_string: str = ""

    while secret_index < len(secret_word) and guess_index < len(user_guess):
        if user_guess[guess_index] == secret_word[secret_index]:
            # if the first letter of the guess is the same as the first letter of the secret word, add a green square to the string that will be printed
            return_string += GREEN_BOX
            guess_index += 1
        else:
            while secret_index < len(secret_word):
                secret_index += 1
                if user_guess[guess_index] == secret_word[secret_index]:
                    return_string += YELLOW_BOX
            else:
                return_string += WHITE_BOX
        guess_index += 1
    return return_string


# need to turn our word into emojis
# compare the first letter of the guess to every letter of the secret word
# based on that, add the first emoji to the return string
# then move onto comparing the second letter of the guess

# present: bool = False
# establish guess_index here --> IT DOES NOT CHANGE until the entire first loop is done
# while secret_index < len (secret word):
# while guess[guess_index] != secret_word[secret_index]
# secret_index +1
# if guess[guess_index] == secret_word[secret_index]
# add green square to str

# while guess_index < len(user_guess):

# while


# green square condition
# if guess[guess_index] == secret_word[secret_index]
# add green square to str
# yellow square condition
# if present = True and if guess[guess_index] != secret_word[secret_index]
# add yellow squre to str
# grey squre condition
# if present = False
# add grey sqaure to str
