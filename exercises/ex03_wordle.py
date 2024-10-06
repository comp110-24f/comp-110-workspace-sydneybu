"""ex03 - wordle- a word guessing game"""

__author__ = "730753182"


def input_guess(secret_word_len: int) -> str:
    """asks the user to input a word of a specified length"""

    # make variable of user guess that takes the players input
    user_guess: str = input(f"Enter a {secret_word_len} character word: ")

    # makes sure the player only enters a word of the right length
    while len(user_guess) != secret_word_len:
        user_guess = input((f"That wasn't {secret_word_len} chars! Try again: "))
    else:
        return user_guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """checks a word to see if it contains a character"""
    # assert only lets the player enter in a single character
    assert len(char_guess) == 1
    index: int = 0

    # while the index number is less than the secret word (so while our index is
    # still in the bounds of the word)
    while index < len(secret_word):
        if char_guess == secret_word[index]:
            # function returns True if the character is in the word
            return True
        else:
            # moves to the next letter of the secret word
            index += 1
    # if True was never returned, False will be returned (the char_guess was not in the secret word)
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """find instances of the guess in the secret word, and print emojis to show if
    their letters were right, in the right place, or totally wrong"""
    # makes sure user input is the same length as the secret word
    assert len(user_guess) == len(secret_word)

    # emoji codes
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    # initializations
    index: int = 0
    return_string: str = ""

    # while our index is still within the bounds of the length of our word
    while index < len(user_guess):
        # if the secret word has the first chracter from the user's guess,
        # we will either print a yellow or green square
        if contains_char(secret_word=secret_word, char_guess=user_guess[index]) == True:

            # if that first character is the same as the first character of the secret word, green square!
            if user_guess[index] == secret_word[index]:
                return_string += GREEN_BOX
                index += 1  # move to the next letter

            # otherwise, yellow square
            else:
                return_string += YELLOW_BOX
                index += 1  # move to the next letter

        # if that first character is not in the secret word at all, then a grey square will be printed
        else:
            return_string += WHITE_BOX
            index += 1  # move to the next letter

    # return the entire string of colored squares
    return return_string


def main(secret: str) -> None:
    """combines all the previous functions to make a playable game of wordle"""

    # start turn at 1
    turn: int = 1

    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_word_len=len(secret))

        # check if the guess is correct
        if guess == secret:
            print(emojified(user_guess=guess, secret_word=secret))
            print(f"You won in {turn}/6 turns!")
            return

        # display the emoji result
        print(emojified(user_guess=guess, secret_word=secret))

        # move to next turn
        turn += 1

    # if they run out of turns
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
