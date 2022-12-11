from random import sample

def bingo():
    while True:
        numbers = sample(range(1,11),3) + sample(range(11,21),2)
        new_list = numbers[:3].copy()
        new_list.sort()
        if new_list == [1,2,3]:
            continue
        else:
            return numbers