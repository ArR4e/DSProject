from random import sample

def bingo():
    esi_kolm = sample(range(1, 11), 3)
    while 1 in esi_kolm and 2 in esi_kolm and 3 in esi_kolm:
        esi_kolm = sample(range(1, 11), 3)
    vim_kaks = sample(range(11, 21), 2)
    
    return esi_kolm + vim_kaks