def lessen(my_list: list[int]):
    idx: int = 0
    while idx < len(my_list):
        my_list[idx] = my_list[idx] - 1
        idx += 1


msg: list[int] = [4, 5, 6]
lessen(msg)
