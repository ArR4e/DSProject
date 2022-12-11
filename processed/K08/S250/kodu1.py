from random import sample
def bingo():
    järjend = []
    while True:
        vahemik_1 = (sample(range(1, 11), 3))
        if sum(vahemik_1) == 6:
            continue
        vahemik_2 = (sample(range(11, 21), 2))
        järjend = vahemik_1 + vahemik_2
        return järjend