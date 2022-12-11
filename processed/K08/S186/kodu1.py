from random import sample
def bingo():
    esimene_osa=sample(range(1, 11), 3)
    while True:
        if sum(esimene_osa) == 6:
            esimene_osa=sample(range(1, 11), 3)
        else:
            break
    teine_osa=sample(range(11, 21), 2)
    return esimene_osa+teine_osa