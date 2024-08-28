"""function that prompts for a message and mimics it back"""

__author__ = "730753182"


def mimic(message: str) -> str:
    """returns the message back to user"""
    return message


def main() -> None:
    """prints the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
