from random import randint

def minu_shuffle(järjend):
    el_arv = len(järjend)
    indeks = 0
    for el in järjend:
        juhuslik_arv = randint(0, el_arv - 1)
        järjend[indeks], järjend[juhuslik_arv] = järjend[juhuslik_arv], järjend[indeks]
        indeks += 1

