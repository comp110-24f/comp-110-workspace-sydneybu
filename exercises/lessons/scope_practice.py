def remove_chars(msg: str, char: str) -> str:
    """return a copy of msg with all instances of char removed"""
    copy: str = ""
    # set up empty string to copy values over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
            # or can be written as copy = copy + msg[index]
        index += 1
        # relative reassignment operator
    return copy


if __name__ == "__main__":
    # if you're running the scope_practice module itself (so not from an import)
    # global variable
    word: str = "yoyo"
    print(remove_chars(word, "o"))
    print(word)
