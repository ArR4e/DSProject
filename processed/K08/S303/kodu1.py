def bingo():
    from random import sample
    while True:
        bingo_list = sample(range(1,11), 3) + sample(range(11,21), 2)
        if {1, 2, 3} & set(bingo_list) == {1, 2, 3}: continue
        break
    return bingo_list

