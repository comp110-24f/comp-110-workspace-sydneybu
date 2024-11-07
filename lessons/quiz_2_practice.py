x: list[int] = [1, 2, 3, 4]


for item in range(0, len(x)):
    print(f"{item}:{x[item]}")

# can't have one dictionary as the value for a key

dict2: dict[int, int] = {
    1: 40
}
dict: dict[int, int] = {
    1: 10
    2: 20
    3: 30
    4: dict2
}


int(7**0.5)