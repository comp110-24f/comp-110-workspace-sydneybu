"""user inputs a number to guess a secret number, and the code tells them if they were right/too high/too low"""

__author__ = "730753182"


def guess_a_number() -> None:
    secret: int = 7
    guess: int = int(input("Guess a number: "))
    # input is taken as a string, so you have to convert it to an int right here so that you can later compare two ints
    print("Your guess was " + str(guess))
    # cant concatenate/add a string and an int, so we temporarily make it a string
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is " + str(secret))
        # same issue with printing an int/string here
    else:
        print("Your guess was too high! The secret number is " + str(secret))
        # and here!


if __name__ == "__main__":
    guess_a_number()
