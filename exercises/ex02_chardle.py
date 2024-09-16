"""ex02 - chardle- a cute step towards wordle"""

__author__ = "730753182"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    # takes the user's input and stores it as the local variable word_5
    if len(word) == 5:  # checks length of word
        print("'" + word + "'")  # i think this is the only way to get
        # those single quotes around the returned word??
        return word
    else:
        print("Error: Word must contain 5 characters.")
        print("'" + word + "'")
        return word


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    # takes the user's input as stores it as the local variable chatacter
    if len(letter) == 1:  # checks length to make sure it is just a character
        print("'" + letter + "'")
        return letter
    else:
        print("Error: Character must be a single chatacter.")
        print("'" + letter + "'")
        return letter


def contains_char(word: str, letter: str) -> None:
    # word = input_word()
    # letter = input_letter()
    print("Searching for " + letter + " in " + word)
    if letter == word[0]:
        print(letter + " found at index 0")
    elif letter == word[1]:
        print(letter + " found at index 1")
    elif letter == word[2]:
        print(letter + " found at index 2")
    elif letter == word[3]:
        print(letter + " found at index 3")
    elif letter == word[4]:
        print(letter + " found at index 4")
    elif letter == word[5]:
        print(letter + " found at index 5")


# input_word()
# input_letter()
# contains_char(word="kitty", letter="t")
