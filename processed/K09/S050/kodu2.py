def minu_shuffle(järjend):
    from random import randint
    for indeks in järjend:
        indeks1=randint(0,len(järjend)-1)
        indeks2=randint(0,len(järjend)-1)
        järjend[indeks1],järjend[indeks2]=järjend[indeks2],järjend[indeks1]