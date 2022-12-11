from random import sample

def bingo():
    kuni_kümme = sample(range(1,10),3)
    if kuni_kümme == [1,2,3]:
        kuni_kümme = sample(range(1,10),3)
    kuni_kakskümmend = sample(range(11,20),2)
    summa = kuni_kümme + kuni_kakskümmend
    return summa
    