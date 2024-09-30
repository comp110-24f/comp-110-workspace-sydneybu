"""puts together two strings"""

__author__ = "730753182"

if __name__ == "__main__":
    # to prevent these variables from being used in the import of concatenation
    word1: str = "happy"
    word2: str = "tuesday"


def concat(input1: str, input2: str) -> str:
    print(input1 + input2)
    return input1 + input2
