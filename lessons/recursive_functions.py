# factorial
def factorial(n: int) -> int:
    """calculate factorial of int n"""
    # edge case
    if n < 0:
        return -1
    # base case
    if n == 1 or n == 0:
        return 1
    # recursive case
    if n >= 1:
        return n * factorial(n - 1)


print(factorial(6))
print(factorial(0))
print(factorial(-1))


# all good function, quiz 04 review
def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    """determine if all dogs were good in daycare"""
    is_good: bool = int(scores[idx]["score"]) >= thresh:
    is_last: bool = idx == len(scores)-1
    # assign true if index is the last idx in scores

    # if the dog is good...
    if is_good == True:
        # print "Good dog, <dog name>!"
        print(f"Good dog, {scores[idx]["name"]}!")
        # is it the last dog?
        if is_last == True:
            # yes = base case
            return True
        # no = recursive case
        else:
            return all_good(scores, thresh, idx + 1)
    # otherwise .. 2nd base case
    else:
        return False
    
pack: list[dict[str,str]] = [
    {"name" : "Nelli", "score" : "10"},
    {"name" : "Ada", "score" : "9"},
    {"name" : "Pip", "score" : "7"}
]