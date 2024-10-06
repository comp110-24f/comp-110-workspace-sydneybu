"""ex02 - chardle- a cute step towards wordle"""

__author__ = "730753182"


def input_word() -> str:
    word: str = input("Enter a 5-character word: ")
    # takes the user's input and stores it as the local variable word_5
    if len(word) == 5:  # checks length of word
        # print("'" + word + "'")  # i think this is the only way to get
        # those single quotes around the returned word??
        return word
    else:
        print("Error: Word must contain 5 characters.")
        # print("'" + word + "'")
        # exit the whole function if the user inputs something other than a 5 letter word
        exit()


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    # takes the user's input as stores it as the local variable chatacter
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    # make a variable to count the number of times a letter appeared
    count: int = 0
    # the below if statements search the word for the letter
    # can't use if/elif because once an elif statement is true, it won't run the rest
    if letter == word[0]:
        print(letter + " found at index 0")
        count = count + 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count = count + 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count = count + 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count = count + 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count = count + 1

    if count == 0:
        print("No instances of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
