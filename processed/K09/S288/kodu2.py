from random import randint

def minu_shuffle(järjend):
    for i in range(len(järjend) - 1, 0, -1):
        juhuslik_arv = randint(0, i)
        järjend[i], järjend[juhuslik_arv] = järjend[juhuslik_arv], järjend[i]

järjend = input('Sisestage järjend: ').split()