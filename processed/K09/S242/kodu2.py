from random import randint

def minu_shuffle(järjend):
    järjendi_pikkus = len(järjend)
    for el in järjend:
        juhuslik_arv = randint(0,(järjendi_pikkus - 1))
        elemendi_indeks = järjend.index(el)
        järjend[elemendi_indeks], järjend[juhuslik_arv] = järjend[juhuslik_arv], järjend[elemendi_indeks]

