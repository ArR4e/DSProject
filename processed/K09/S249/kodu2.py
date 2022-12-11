from random import randint

def minu_shuffle(järjend):
    
    for indeks in range(len(järjend) - 1, 0, -1):
        suvalinearv = randint(0, indeks)
        if suvalinearv == indeks:
            continue
        else:
            järjend[indeks], järjend[suvalinearv] = järjend[suvalinearv], järjend[indeks]
    