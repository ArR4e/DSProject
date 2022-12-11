from random import sample
def bingo():
    järjend=[]
    ühest=sample(range(1, 11), 3)
    kümnest= sample(range(11, 21), 2)
    while True:
        if 3 in ühest and 2 in ühest and 1 in ühest:
            ühest=sample(range(1, 11), 3)
        else:
            break
    järjend=ühest+kümnest
    return järjend