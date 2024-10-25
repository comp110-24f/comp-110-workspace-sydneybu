"""ex06- dictionary utility functions"""

__author__ = "730753182"


def invert(input: dict[str, str]) -> dict[str, str]:
    """return a dictionary of strings that has inverted the keys and values of the input"""
    inverse_dict: dict[str, str] = {}

    # iterates through the keys of the dictionary "input"
    for item in input:
        value = input[item]
        # KeyError if the value is already in the new dictionary
        if value in inverse_dict:
            raise KeyError(f"Duplicate value found: {value}")
        # add the value to the new dictionary, but now the value is the key
        inverse_dict[value] = item
    return inverse_dict


def favorite_color(input: dict[str, str]) -> str:
    """return a str of the most frequent value in the dictionary input"""
    color_count: dict[str, int] = {}

    # count the number of occurences for each color
    for name in input:
        color = input[name]
        # if the value in in our new dict, add 1 to the count
        if color in color_count:
            color_count[color] += 1
        # otherwise, add the value to the dict with a count of 1
        else:
            color_count[color] = 1

    # find the color with the highest number of occurences
    favorite_color: str = ""
    highest_num: int = 0

    # iterate through our dict of colors and their counts
    for color in color_count:
        count: int = color_count[color]
        # if # occurances of the color is < highest num
        if count > highest_num:
            # that # is now the highest num
            highest_num = count
            # and our new favorite color is that color
            favorite_color = color

    return favorite_color


def count(input: list[str]) -> dict[str, int]:
    """make a dictionary where the key is a string in a list, and the value is the number of times that value was in the list"""
    result: dict[str, int] = {}

    # iterates through the list
    for elem in input:
        # if the str is already in the dict, add 1 to count
        if elem in result:
            result[elem] += 1
        # if not, add the str to the dict and make the count = 1
        else:
            result[elem] = 1
    return result


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """make a dictionary of letters and the words that start w that letter from the input list"""
    result: dict[str, list[str]] = {}

    # iterates through the input list
    for word in input:
        # make a variable that is the first letter of each word in lowercase
        letter: str = word[0].lower()
        # if the letter is already in the dict, add that word to the value list
        if letter in result:
            result[letter].append(word)
        # otherwise, make a new key in the dict
        else:
            result[letter] = [word]
    return result


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """given an attendance dict of day of the week and present students, add a student to the dict based on the day"""
    # if they day is already in the attendance, add that student
    if day in input:
        input[day].append(student)
    # if the day in not in attendance, make a new key-value pair
    else:
        input[day] = [student]
