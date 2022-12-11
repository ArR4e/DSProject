from random import sample
def bingo():
    järjend = []
    i = 0
    while True:
        arv_1_10 = sample(range(1, 11), 3)
        for arv in arv_1_10:
            if arv in [1, 2, 3]: # Kui genereeritud arv on antud järjendi sees
                i += 1
        if i == 3:
            continue
        else:
            break
    arv_11_20 = sample(range(11, 21), 2)
    järjend = arv_1_10 + arv_11_20
    return järjend