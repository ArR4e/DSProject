from random import sample
def bingo():
    while True:
        list_1 = sample(range(1,11),3) + sample(range(11,21),2)
        list_2 = sorted(list_1)
        if list_2[0] == 1 and list_2[1] == 2 and list_2[2] == 3:
            continue
        else:
            break
    return list_1
