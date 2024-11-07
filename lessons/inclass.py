def sum(num1: int, num2: int) -> int:
    """add two numbers together"""
    return num1 + num2


sum(num1=11, num2=3)


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "no match"


def get_weather_report() -> str:
    weather: str = input("What is the weather?")
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather")
    return weather


get_weather_report()



if count >= 1:
        print(str(count) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)
